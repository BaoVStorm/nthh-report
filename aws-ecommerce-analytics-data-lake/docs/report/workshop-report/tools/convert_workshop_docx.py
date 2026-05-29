from __future__ import annotations

import html
import re
import shutil
import zipfile
from dataclasses import dataclass, field
from pathlib import Path
from xml.etree import ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
DOCX = ROOT / "DRAFT internship workshop report.docx"
CONTENT_ROOT = ROOT / "content" / "5-Workshop"
STATIC_IMAGE_ROOT = ROOT / "static" / "images" / "5-Workshop"

NS = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "rel": "http://schemas.openxmlformats.org/package/2006/relationships",
}

W_VAL = f"{{{NS['w']}}}val"
R_EMBED = f"{{{NS['r']}}}embed"


@dataclass(frozen=True)
class SectionSpec:
    folder: str
    title: str
    start_title: str | None
    weight: int


@dataclass
class Element:
    kind: str
    text: str = ""
    style: str = ""
    numid: str = ""
    ilvl: int = 0
    image_rids: list[str] = field(default_factory=list)
    rows: list[list[str]] = field(default_factory=list)


SECTIONS = [
    SectionSpec("5.1-Gioi-thieu", "5.1. Giới thiệu", None, 510),
    SectionSpec("5.2-Kaggle-Dataset-preprocessing-o-local", "5.2. Kaggle Dataset preprocessing ở local", "Kaggle Dataset preprocessing ở local", 520),
    SectionSpec("5.3-Tao-S3-Raw-Zone", "5.3. Tạo S3 Raw Zone", "Tạo S3 Raw Zone", 530),
    SectionSpec("5.4-Tao-Glue-Data-Catalog-cho-raw-data", "5.4. Tạo Glue Data Catalog cho raw data", "Tạo Glue Data Catalog cho raw data", 540),
    SectionSpec("5.4.1-Tao-IAM-Role-cho-AWS-Glue", "5.4.1. Tạo IAM Role cho AWS Glue", "Tạo IAM Role cho AWS Glue", 541),
    SectionSpec("5.4.2-Tao-Glue-Database", "5.4.2. Tạo Glue Database", "Tạo Glue Database", 542),
    SectionSpec("5.5-Tao-Glue-Crawler-cho-Raw-Data", "5.5. Tạo Glue Crawler cho Raw Data", "Tạo Glue Crawler cho Raw Data", 550),
    SectionSpec("5.6-Cau-hinh-Athena-query-result-location", "5.6. Cấu hình Athena query result location", "Cấu hình Athena query result location", 560),
    SectionSpec("5.7-Glue-ETL-Job", "5.7. Glue ETL Job", "Glue ETL Job", 570),
    SectionSpec("5.7.2-Tao-Glue-ETL-Job", "5.7.2. Tạo Glue ETL Job", "Tạo Glue ETL Job", 572),
    SectionSpec("5.7.3-Kiem-tra-output-tren-Amazon-S3", "5.7.3. Kiểm tra output trên Amazon S3", "Kiểm tra output trên Amazon S3", 573),
    SectionSpec("5.8-Tao-Glue-Data-Catalog-cho-Curated-Data", "5.8. Tạo Glue Data Catalog cho Curated Data", "Tạo Glue Data Catalog cho Curated Data", 580),
    SectionSpec("5.8.1-Tao-Glue-Database-ecommerce-curated", "5.8.1. Tạo Glue Database ecommerce_curated", "Tạo Glue Database ecommerce_curated", 581),
    SectionSpec("5.8.2-Tao-Glue-Crawler-cho-du-lieu-Curated-Parquet", "5.8.2. Tạo Glue Crawler cho dữ liệu Curated Parquet", "Tạo Glue Crawler cho dữ liệu Curated Parquet", 582),
    SectionSpec("5.8.3-Chay-Glue-Crawler", "5.8.3. Chạy Glue Crawler", "Chạy Glue Crawler", 583),
    SectionSpec("5.8.4-Query-Curated-Tables-trong-Athena", "5.8.4. Query Curated Tables trong Athena", "Query Curated Tables trong Athena", 584),
    SectionSpec("5.9-Validate-curated-data", "5.9. Validate curated data", "Validate curated data", 590),
    SectionSpec("5.10-Tao-Athena-Views-cho-analytics", "5.10. Tạo Athena Views cho analytics", "Tạo Athena Views cho analytics", 600),
    SectionSpec("5.11-Ket-noi-QuickSight-voi-Athena", "5.11. Kết nối QuickSight với Athena", "Kết nối QuickSight với Athena", 610),
    SectionSpec("5.12-Dashboard-1-Executive-Overview", "5.12. Dashboard 1 - Executive Overview", "Dashboard 1 — Executive Overview", 620),
    SectionSpec("5.13-Dashboard-2-Funnel-Analytics", "5.13. Dashboard 2: Funnel Analytics", "Dashboard 2: Funnel Analytics", 630),
    SectionSpec("5.14-Dashboard-3-Marketing-Performance", "5.14. Dashboard 3: Marketing Performance", "Dashboard 3: Marketing Performance", 640),
    SectionSpec("5.15-Dashboard-4-Product-Analytics", "5.15. Dashboard 4: Product Analytics", "Dashboard 4: Product Analytics", 650),
    SectionSpec("5.16-Dashboard-5-AB-Testing", "5.16. Dashboard 5: A/B Testing", "Dashboard 5: A/B Testing", 660),
    SectionSpec("5.17-Publish-Dashboards", "5.17. Publish Dashboards", "Publish Dashboards", 670),
    SectionSpec("5.18-Automation-and-Monitoring-Layer", "5.18. Automation & Monitoring Layer", "Automation & Monitoring Layer", 680),
    SectionSpec("5.18.1-Tao-SNS-Email-Notification", "5.18.1. Tạo SNS Email Notification", "Tạo SNS Email Notification", 681),
    SectionSpec("5.18.2-Tao-Glue-Workflow", "5.18.2. Tạo Glue Workflow", "Tạo Glue Workflow", 682),
    SectionSpec("5.18.3-Kiem-tra-CloudWatch-Logs-cho-Glue-ETL-Job", "5.18.3. Kiểm tra CloudWatch Logs cho Glue ETL Job", "Kiểm tra CloudWatch Logs cho Glue ETL Job", 683),
    SectionSpec("5.18.4-Su-dung-EventBridge-de-schedule", "5.18.4. Sử dụng EventBridge để schedule", "Sử dụng EventBridge để schedule", 684),
    SectionSpec("5.18.5-Kiem-tra-schedule", "5.18.5. Kiểm tra schedule", "Kiểm tra schedule", 685),
    SectionSpec("5.18.6-EventBridge-Rule-dung-de-alert-loi", "5.18.6. EventBridge Rule dùng để alert lỗi", "EventBridge Rule dùng để alert lỗi", 686),
]

START_TO_SECTION = {s.start_title: s for s in SECTIONS if s.start_title}
START_TITLES = set(START_TO_SECTION)


def extract_paragraph_text(p: ET.Element) -> str:
    parts: list[str] = []
    for node in p.iter():
        tag = node.tag.rsplit("}", 1)[-1]
        if tag == "t":
            parts.append(node.text or "")
        elif tag == "tab":
            parts.append("\t")
        elif tag in {"br", "cr"}:
            parts.append("\n")
    return re.sub(r"[ \t]+\n", "\n", "".join(parts)).strip()


def paragraph_meta(p: ET.Element) -> tuple[str, str, int]:
    pstyle = p.find("./w:pPr/w:pStyle", NS)
    style = pstyle.get(W_VAL, "") if pstyle is not None else ""
    numpr = p.find("./w:pPr/w:numPr", NS)
    if numpr is None:
        return style, "", 0
    numid_el = numpr.find("./w:numId", NS)
    ilvl_el = numpr.find("./w:ilvl", NS)
    numid = numid_el.get(W_VAL, "") if numid_el is not None else ""
    ilvl = int(ilvl_el.get(W_VAL, "0")) if ilvl_el is not None else 0
    return style, numid, ilvl


def extract_cell_text(cell: ET.Element) -> str:
    texts: list[str] = []
    for p in cell.findall(".//w:p", NS):
        text = extract_paragraph_text(p)
        if text:
            texts.append(text)
    return "\n".join(texts).strip()


def read_relationships(zf: zipfile.ZipFile) -> dict[str, str]:
    rels: dict[str, str] = {}
    root = ET.fromstring(zf.read("word/_rels/document.xml.rels"))
    for rel in root.findall("rel:Relationship", NS):
        rid = rel.attrib.get("Id")
        target = rel.attrib.get("Target", "")
        if rid and target.startswith("media/"):
            rels[rid] = "word/" + target
    return rels


def read_docx() -> tuple[list[Element], dict[str, str]]:
    elements: list[Element] = []
    with zipfile.ZipFile(DOCX) as zf:
        rels = read_relationships(zf)
        root = ET.fromstring(zf.read("word/document.xml"))
        body = root.find("w:body", NS)
        if body is None:
            raise RuntimeError("Cannot find Word document body")
        for child in body:
            tag = child.tag.rsplit("}", 1)[-1]
            if tag == "p":
                text = extract_paragraph_text(child)
                image_rids = [b.get(R_EMBED) for b in child.findall(".//a:blip", NS) if b.get(R_EMBED)]
                if not text and not image_rids:
                    continue
                style, numid, ilvl = paragraph_meta(child)
                elements.append(Element("p", text=text, style=style, numid=numid, ilvl=ilvl, image_rids=image_rids))
            elif tag == "tbl":
                rows: list[list[str]] = []
                for tr in child.findall("./w:tr", NS):
                    row = [extract_cell_text(tc) for tc in tr.findall("./w:tc", NS)]
                    if any(cell for cell in row):
                        rows.append(row)
                if rows:
                    elements.append(Element("table", rows=rows))
    return elements, rels


def split_sections(elements: list[Element]) -> dict[str, list[Element]]:
    buckets = {s.folder: [] for s in SECTIONS}
    current = SECTIONS[0]
    for el in elements:
        if el.kind == "p" and el.text in START_TO_SECTION:
            current = START_TO_SECTION[el.text]
            continue
        buckets[current.folder].append(el)
    return buckets


def language_for_code(text: str) -> str:
    stripped = text.strip()
    upper = stripped.upper()
    if upper.startswith(("SELECT ", "WITH ", "CREATE ", "ALTER ", "INSERT ", "DROP ")) or "\nSELECT " in upper:
        return "sql"
    if stripped.startswith(("{", "[")) and any(ch in stripped for ch in ['"', ":"]):
        return "json"
    if re.search(r"(^|\n)\s*(from pyspark|import |def |class |spark\.|glueContext|args\s*=)", stripped):
        return "python"
    if re.search(r"(^|\n)\s*(aws |pip |python |mkdir |cp |export )", stripped):
        return "bash"
    return ""


def looks_like_code(text: str) -> bool:
    return bool(language_for_code(text))


def render_code(text: str) -> str:
    lang = language_for_code(text)
    return f"```{lang}\n{text.strip()}\n```"


def escape_table_cell(text: str) -> str:
    text = text.replace("\n", "<br>")
    return text.replace("|", "\\|").strip()


def render_table(rows: list[list[str]]) -> str:
    max_cols = max(len(row) for row in rows)
    normalized = [row + [""] * (max_cols - len(row)) for row in rows]
    if max_cols == 1:
        text = "\n".join(row[0] for row in normalized if row[0]).strip()
        if looks_like_code(text):
            return render_code(text)
        return text
    header = normalized[0]
    body = normalized[1:] or [[""] * max_cols]
    lines = [
        "| " + " | ".join(escape_table_cell(c) for c in header) + " |",
        "| " + " | ".join("---" for _ in range(max_cols)) + " |",
    ]
    for row in body:
        lines.append("| " + " | ".join(escape_table_cell(c) for c in row) + " |")
    return "\n".join(lines)


def render_paragraph(el: Element, spec: SectionSpec, image_counter: list[int], rels: dict[str, str], zf: zipfile.ZipFile) -> list[str]:
    rendered: list[str] = []
    text = el.text.strip()

    if text:
        if looks_like_code(text):
            rendered.append(render_code(text))
        elif el.style.startswith("Heading"):
            rendered.append(f"### {text}")
        elif el.numid == "1" and el.ilvl > 0:
            level = min(2 + el.ilvl, 4)
            rendered.append(f"{'#' * level} {text}")
        elif el.numid and el.numid != "1":
            indent = "  " * max(el.ilvl, 0)
            for line in text.splitlines():
                rendered.append(f"{indent}- {line.strip()}")
        else:
            rendered.append(text)

    for rid in el.image_rids:
        source = rels.get(rid)
        if not source:
            continue
        image_counter[0] += 1
        ext = Path(source).suffix or ".png"
        image_name = f"image-{image_counter[0]:03d}{ext}"
        image_dir = STATIC_IMAGE_ROOT / spec.folder
        image_dir.mkdir(parents=True, exist_ok=True)
        target = image_dir / image_name
        with zf.open(source) as src, target.open("wb") as dst:
            shutil.copyfileobj(src, dst)
        rendered.append(f"![](/images/5-Workshop/{spec.folder}/{image_name})")

    return rendered


def front_matter(title: str, weight: int) -> str:
    return (
        "---\n"
        f'title: "{title}"\n'
        "date: 2026-05-29\n"
        f"weight: {weight}\n"
        "chapter: false\n"
        "---\n\n"
    )


def write_section(spec: SectionSpec, elements: list[Element], rels: dict[str, str]) -> None:
    section_dir = CONTENT_ROOT / spec.folder
    section_dir.mkdir(parents=True, exist_ok=True)

    english = front_matter(spec.title, spec.weight) + f"# {spec.title}\n\nContent will be added in English later.\n"
    (section_dir / "_index.md").write_text(english, encoding="utf-8", newline="\n")

    lines = [front_matter(spec.title, spec.weight).rstrip(), "", f"# {spec.title}"]
    if spec.folder == "5.1-Gioi-thieu" and not elements:
        lines += ["", "Phần này dùng để viết giới thiệu workshop."]

    image_counter = [0]
    with zipfile.ZipFile(DOCX) as zf:
        for el in elements:
            if el.kind == "p":
                blocks = render_paragraph(el, spec, image_counter, rels, zf)
            else:
                blocks = [render_table(el.rows)]
            for block in blocks:
                if block:
                    lines.extend(["", block])

    (section_dir / "_index.vi.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")


def tree(path: Path) -> str:
    lines = [path.name + "/"]
    children = sorted(path.iterdir(), key=lambda p: (not p.is_dir(), p.name.lower()))

    def walk(items: list[Path], prefix: str) -> None:
        for i, item in enumerate(items):
            connector = "└── " if i == len(items) - 1 else "├── "
            lines.append(prefix + connector + item.name + ("/" if item.is_dir() else ""))
            if item.is_dir():
                sub = sorted(item.iterdir(), key=lambda p: (not p.is_dir(), p.name.lower()))
                walk(sub, prefix + ("    " if i == len(items) - 1 else "│   "))

    walk(children, "")
    return "\n".join(lines)


def main() -> None:
    if not DOCX.exists():
        raise FileNotFoundError(DOCX)
    CONTENT_ROOT.mkdir(parents=True, exist_ok=True)
    STATIC_IMAGE_ROOT.mkdir(parents=True, exist_ok=True)

    elements, rels = read_docx()
    buckets = split_sections(elements)
    for spec in SECTIONS:
        write_section(spec, buckets[spec.folder], rels)

    starts_found = {el.text for el in elements if el.kind == "p" and el.text in START_TITLES}
    missing = sorted(START_TITLES - starts_found)
    print(f"Converted {len(SECTIONS)} sections.")
    print(f"Extracted images to: {STATIC_IMAGE_ROOT}")
    if missing:
        print("Missing mapped starts:")
        for title in missing:
            print(f"- {title}")
    print()
    print(tree(CONTENT_ROOT))


if __name__ == "__main__":
    main()
