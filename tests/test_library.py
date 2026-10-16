import sys
import unittest
import tempfile
import json
from unittest.mock import patch
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from library import identities, parse_atom, parse_bibtex, title_identity
from discover import merge_hits
from discover import parse_datacite
import discover


class LibraryTests(unittest.TestCase):
    def test_nested_bibtex_and_adjacent_entries(self):
        s = '@article{a, title={{RL}: An {MTP} Study},year={2026}}@article{b,title={Other},year="2025"}'
        records = parse_bibtex(s)
        self.assertEqual([r["id"] for r in records], ["a", "b"])
        self.assertEqual(records[0]["fields"]["title"], "{RL}: An {MTP} Study")

    def test_same_arxiv_new_key_not_new_study(self):
        p = {"id": "old", "title": "Old title", "arxiv_id": "2609.12345", "reviewed_version": "v1"}
        hit = {"arxiv_id": "2609.12345", "version": "v2", "title": "A changed title", "updated": "2026-10-16T00:00:00Z", "url": "https://arxiv.org/abs/2609.12345v2", "queries": ["primary"]}
        queue, versions, count = merge_hits([hit], [p], [], [])
        self.assertEqual(queue, [])
        self.assertEqual(count, 0)
        self.assertEqual(versions[0]["observed_version"], "v2")

    def test_title_dedup_and_rejection_memory(self):
        hit = {"arxiv_id": "2609.12345", "version": "v1", "title": "An RL Survey", "updated": "2026-10-16T00:00:00Z", "queries": ["primary"]}
        self.assertEqual(merge_hits([hit], [{"id": "known", "title": "An {RL} Survey"}], [], [])[2], 0)
        log = [{"decision": "excluded", "identities": list(identities(hit))}]
        self.assertEqual(merge_hits([hit], [], [], log)[0], [])

    def test_query_overlap_is_one_candidate(self):
        a = {"arxiv_id": "2609.12345", "version": "v1", "title": "A", "updated": "2026-10-16T00:00:00Z", "queries": ["one"]}
        b = {**a, "queries": ["two"]}
        queue, _, count = merge_hits([a, b], [], [], [])
        self.assertEqual(count, 1)
        self.assertEqual(queue[0]["queries"], ["one", "two"])

    def test_atom_error_is_not_empty_search(self):
        with self.assertRaises(ValueError):
            parse_atom('<feed xmlns="http://www.w3.org/2005/Atom"><entry><id>http://arxiv.org/api/errors</id></entry></feed>')

    def test_html_is_not_a_successful_empty_feed(self):
        with self.assertRaises(ValueError):
            parse_atom('<html><body>Too many requests</body></html>')

    def test_registry_date_does_not_erase_paper_version(self):
        paper = {"arxiv_id": "2609.12345", "version": "v2", "title": "A", "updated": "2026-10-01T00:00:00Z", "queries": ["arxiv"]}
        registry = {**paper, "version": "", "updated": "2026-10-16T00:00:00Z", "queries": ["registry"], "metadata_source": "DataCite"}
        queue, _, _ = merge_hits([paper, registry], [], [], [])
        self.assertEqual(queue[0]["version"], "v2")
        self.assertNotIn("metadata_source", queue[0])

    def test_registry_is_not_an_arxiv_version_observation(self):
        paper = {"id": "known", "arxiv_id": "2609.12345", "title": "A", "reviewed_version": "v1"}
        registry = {"arxiv_id": "2609.12345", "version": "", "title": "A", "updated": "2026-10-16T00:00:00Z", "queries": ["registry"], "metadata_source": "DataCite"}
        self.assertEqual(merge_hits([registry], [paper], [], [])[1], [])

    def test_parse_registry_keeps_provenance(self):
        payload = {"data": [{"attributes": {"doi": "10.48550/arXiv.2609.12345", "titles": [{"title": "A"}], "creators": [{"name": "Researcher"}], "publicationYear": 2026, "updated": "2026-10-16T00:00:00Z"}}], "meta": {"total": 1}}
        records, total = parse_datacite(json.dumps(payload))
        self.assertEqual(total, 1)
        self.assertEqual(records[0]["version"], "")
        self.assertEqual(records[0]["metadata_source"], "DataCite arXiv DOI registry")

    def test_failed_search_preserves_last_successful_watermark(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "data").mkdir()
            for name, value in {"papers": [], "inbox": [], "version_observations": [],
                                "search_queries": {"families": [{"id": "test", "query": "all:speculative"}]},
                                "update_state": {"last_successful_scan": "2026-10-01T00:00:00Z"}}.items():
                (root / f"data/{name}.json").write_text(json.dumps(value))
            with patch.object(discover, "ROOT", root), patch.object(discover, "fetch", side_effect=TimeoutError("source unavailable")), patch.object(discover.time, "sleep"), patch.object(sys, "argv", ["discover"]):
                with self.assertRaises(SystemExit):
                    discover.main()
            state = json.loads((root / "data/update_state.json").read_text())
            self.assertEqual(state["last_successful_scan"], "2026-10-01T00:00:00Z")
            self.assertEqual(state["status"], "incomplete")


if __name__ == "__main__":
    unittest.main()
