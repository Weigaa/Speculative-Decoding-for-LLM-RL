"""Shared bibliography identities and conservative metadata helpers (stdlib only)."""
import html
import json
import re
import unicodedata
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
ATOM = {"a": "http://www.w3.org/2005/Atom", "o": "http://a9.com/-/spec/opensearch/1.1/"}


def read_json(path, default=None):
    return json.loads(path.read_text()) if path.exists() else default


def write_json(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n")


def text(value):
    value = value.replace(r"S$^3$R", "S³R").replace(r"\&", "&")
    return " ".join(value.replace("{", "").replace("}", "").split())


def title_identity(value):
    value = unicodedata.normalize("NFKD", text(value)).casefold()
    return "".join(c for c in value if c.isalnum())


def arxiv_identity(value):
    m = re.search(r"(?:arxiv(?:\.org/(?:abs|pdf)/|:|\.))?(\d{4}\.\d{4,5})(?:v\d+)?", value, re.I)
    return m[1] if m else ""


def doi_identity(value):
    return re.sub(r"^https?://(?:dx\.)?doi\.org/", "", value.strip(), flags=re.I).casefold()


def identities(record):
    result = {"title:" + title_identity(record.get("title", ""))}
    aid = record.get("arxiv_id") or arxiv_identity(record.get("url", ""))
    if aid:
        result.add("arxiv:" + arxiv_identity(aid))
    doi = doi_identity(record.get("doi", ""))
    if doi:
        result.add("doi:" + doi)
        if doi.startswith("10.48550/arxiv."):
            result.add("arxiv:" + arxiv_identity(doi))
    return result - {"title:"}


def md(value):
    value = html.escape(str(value), quote=False)
    return value.replace("|", r"\|").replace("[", r"\[").replace("]", r"\]").replace("\n", " ")


def checked_url(value):
    p = urlparse(value)
    if p.scheme != "https" or not p.netloc or p.username or p.password:
        raise ValueError("Expected a public HTTPS URL")
    return value.replace("(", "%28").replace(")", "%29")


def _balanced(s, pos):
    depth, i = 0, pos
    while i < len(s):
        if s[i] == "\\":
            i += 2
            continue
        if s[i] == "{":
            depth += 1
        elif s[i] == "}":
            depth -= 1
            if depth == 0:
                return i
        i += 1
    raise ValueError("Unbalanced BibTeX braces")


def parse_bibtex(s):
    entries, pos = [], 0
    while m := re.search(r"@(\w+)\s*\{\s*([^,\s]+)\s*,", s[pos:]):
        start = pos + m.start()
        brace = s.index("{", start)
        end = _balanced(s, brace)
        body_start = pos + m.end()
        body, fields, cursor = s[body_start:end], {}, 0
        while f := re.search(r"(\w+)\s*=\s*", body[cursor:]):
            name, begin = f[1].lower(), cursor + f.end()
            if body[begin] == "{":
                finish = _balanced(body, begin)
                value, cursor = body[begin + 1:finish], finish + 1
            elif body[begin] == '"':
                finish = begin + 1
                while finish < len(body) and (body[finish] != '"' or body[finish - 1] == "\\"):
                    finish += 1
                value, cursor = body[begin + 1:finish], finish + 1
            else:
                finish = body.find(",", begin)
                if finish < 0:
                    finish = len(body)
                value, cursor = body[begin:finish], finish + 1
            fields[name] = " ".join(value.split())
        entries.append({"id": m[2], "type": m[1].lower(), "fields": fields, "bibtex": s[start:end + 1]})
        pos = end + 1
    return entries


def parse_atom(xml):
    import xml.etree.ElementTree as ET
    root = ET.fromstring(xml)
    result = []
    for entry in root.findall("a:entry", ATOM):
        get = lambda name: " ".join((entry.findtext("a:" + name, default="", namespaces=ATOM)).split())
        full_id = get("id").rsplit("/", 1)[-1]
        aid = arxiv_identity(full_id)
        if not aid:
            raise ValueError("arXiv response contains an error or a missing identifier")
        result.append({
            "arxiv_id": aid, "version": full_id[len(aid):],
            "title": get("title"), "authors": [x.findtext("a:name", namespaces=ATOM) for x in entry.findall("a:author", ATOM)],
            "published": get("published"), "updated": get("updated"),
            "abstract": get("summary"), "url": "https://arxiv.org/abs/" + full_id,
        })
    total = int(root.findtext("o:totalResults", default=str(len(result)), namespaces=ATOM))
    return result, total
