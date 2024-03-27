from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey
from datetime import datetime
from typing import Union

from models import Base

class Item(Base):
    __tablename__ = 'item'

    id = Column("pk_item", Integer, primary_key=True)
    name = Column(String(2000))
    type = Column(String(10))
    value = Column(Float)
    date_insert = Column(DateTime, default=datetime.now())

    # Definição do relacionamento entre o Items e um Month.
    # Aqui está sendo definido a coluna 'month' que vai guardar
    month = Column(Integer, ForeignKey("month.pk_month"), nullable=False)

    def __init__(self, name: str, type_string: str, value: float, date_insert:Union[DateTime, None] = None):
        """
        Cria um Item
        Arguments:
            name: nome da conta.
            type: tipo da conta.
            value: valor da conta.
            data_insercao: data de quando o comentário foi feito ou inserido
                           à base
        """
        self.name = name
        self.type = type_string
        self.value = value
        if date_insert:
            self.date_insert = date_insert