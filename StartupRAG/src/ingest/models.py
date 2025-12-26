# Documents, Chunks dataclasses
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, Optional

# Domain models used during ingestion. These are immutable (frozen=True)
# to keep them safe for caching and reuse across the pipeline.

@dataclass(frozen=True)
class Document:
    """Represents a single logical source document before chunking."""

    # Required
    document_id: str  # Stable unique identifier for this document
    source: str       # Human-readable source (e.g. filename, URL, collection)
    text: str         # Full raw text content of the document

    # Optional
    metadata: Dict[str, Any] = field(
        default_factory=dict
    )  # Arbitrary key/value metadata (tags, timestamps, etc.)

@dataclass(frozen=True)
class Chunk:
    """Represents a slice of a Document used for retrieval and embedding."""

    chunk_id: str       # Unique identifier for this chunk
    document_id: str    # Foreign key back to the parent Document
    chunk_index: int    # Position of this chunk within the document (0-based)
    content: str        # Text content of the chunk
    
    # Optional  
    metadata: Dict[str, Any] = field(
        default_factory=dict
    )  # Per-chunk metadata (section title, page number, etc.)