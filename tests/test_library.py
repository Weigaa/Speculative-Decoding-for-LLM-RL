import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from library import identities, parse_atom, parse_bibtex, title_identity
from discover import merge_hits


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


if __name__ == "__main__":
    unittest.main()
