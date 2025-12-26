# Documents, Chunks dataclasses
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, Optional

@dataclass(frozen=True)
class Document:

    # Required
    document_id: str
    source: str
    text: str

    # Optional
    metadata: Dict[str, Any] = field(default_factory=dict)

@dataclass(frozen=True)
class Chunk:
    chunk_id: str
    document_id: str
    chunk_index: int
    content: str
    
    # Optional  
    metadata: Dict[str, Any] = field(default_factory=dict)