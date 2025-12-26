# loads raw documents from various sources
from __future__ import annotations

from pathlib import Path
from typing import List

from .models import Document

RAW_DOCUMENTS_DIR = Path.cwd().parent.parent / "data" / "raw_docs"

def _build_document_id(fileName: str) -> str:
    """
    Build a stable internal document identifier from a file name.

    Args:
        fileName: File name without extension.

    Returns:
        A string identifier prefixed with 'doc_'.
    """
    return "doc_" + fileName

def load_text_documents(directory_path: Path | None) -> List[Document]:
    """
    Load all `.txt` files in a directory as `Document` instances.

    If `directory_path` is None, the default RAW_DOCUMENTS_DIR is used.

    Args:
        directory_path: Optional path to a directory containing .txt files.

    Returns:
        A list of Document objects populated with file path, text, and ID.
    """
    documents: List[Document] = []

    if directory_path is None:
        directory_path = RAW_DOCUMENTS_DIR
        
    for file in directory_path.glob("*.txt"):
        with open(file, "r", encoding="utf-8") as f:
            text = f.read()
            document_id = _build_document_id(file.stem)
            document = Document(
                document_id=document_id,
                source=str(file),
                text=text
            )
            documents.append(document)
    return documents