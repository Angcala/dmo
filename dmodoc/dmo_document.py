"""
class for DMO documents
"""

from typing import List
from uuid import UUID
from enum import Enum

class DocType(Enum):
    CHARACTER = "character"
    ITEM = "item"
    MONSTER = "monster"
    DEFAULT = "default"


class DMODocument:
    """ 
        type (DocType) is nullable. If present, it indicates
        certain properties, such as additional fields. 
        Could also be used for display purposes

    """
    def __init__(self):
        self.content: str = None
        self.links: List[UUID] = []
        self.type: DocType = DocType.DEFAULT
        self.id: UUID = UUID()

    
    
