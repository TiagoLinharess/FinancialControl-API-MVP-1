from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from datetime import datetime
from typing import Union

from models import Base

class Month(Base):
    __tablename__ = 'month'

    id = Column("pk_month", Integer, primary_key=True)
    month = Column(String(20))
    date_insert = Column(DateTime, default=datetime.now())

    year = Column(Integer, ForeignKey("year.pk_year"), nullable=False)

    def __init__(self, month: str, date_insert:Union[DateTime, None] = None):
        self.month = month
        if date_insert:
            self.date_insert = date_insert