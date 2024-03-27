from models import Session, Month, Item
from typing import List

class ItemRepository():
    # Propriedade de tipo da conta
    types = ["income", "outcome"]

    # Inicializa repositório
    def __init__(self, session: Session):
        self.__session = session

    # Método create do repositório
    def create(self, month: Month, name: str, type_string: str, value: float):
        if not self.is_valid(type_string):
            raise ValueError("Item is not valid.")

        item = Item(name, type_string, value)
        
        month.add_item(item)
    
    # Método read do repositório
    def read(self, month: Month) -> List[Item]:
        items = self.__session.query(Item).filter(Item.month == month.id).all()
        return items

    # Método delete do repositório
    def delete(self, item_id: int) -> bool:
        count = self.__session.query(Item).filter(Item.id == item_id).delete()

        if count:
            return True
        else:
            return False

    # Método is_valid do repositório
    def is_valid(self, type_string: str) -> bool:
        if type_string in self.types: 
            return True
        else:
            return False