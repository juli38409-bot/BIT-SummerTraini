
from pathlib import Path


class ScanResult:
    def __init__(self, title, pages, source_type="image"):
        self.title = title
        self.pages = pages
        self.source_type = source_type
        self.warnings = []
        self.text_blocks = []


def load_pages(source_path: Path):
    if source_path.is_file():
        return [source_path]

    if source_path.is_dir():
        return sorted(
            [p for p in source_path.iterdir()
             if p.suffix.lower() in {".png", ".jpg", ".jpeg"}]
        )

    raise NotImplementedError("TODO: implement load_pages")


def scan_source(source_path: Path, ocr_engine=None, warn_threshold=0.0):
    pages = load_pages(source_path)

    title = source_path.stem

    processed_pages = []

    for i, page in enumerate(pages):
        processed_pages.append({
            "page": f"page_{i}",
            "source": str(page),
            "type": "image",
            "ocr_engine": ocr_engine,
        })

    return ScanResult(
        title=title,
        pages=processed_pages,
        source_type="image"
    )