import json
from models import Item
from typing import List

class ItemSchema:

    # Inicializa response
    def __init__(self, item: Item):
        self.name: str = item.name
        self.type: str = item.type
        self.value: str = item.value
    
    # Transforma objeto em json
    def to_json(self):
        return {
            "name": self.name,
            "type": self.type,
            "value": self.value
        }
