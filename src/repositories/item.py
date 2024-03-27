from models import Session, Month, Item

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
    
    # # Método read do repositório
    # def read(self, year: Year) -> [Month]:
    #     months = self.__session.query(Month).filter(Month.year == year.id).all()
    #     return months

    # Método is_valid do repositório
    def is_valid(self, type_string: str) -> bool:
        if type_string in self.types: 
            return True
        else:
            return False