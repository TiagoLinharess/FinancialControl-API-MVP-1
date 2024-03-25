from models import Session, Year

class YearRepository():

    def __init__(self):
        self.__session = Session()

    def create(self, year_string: str):
        year = Year(year_string)
        self.__session.add(year)
        self.__session.commit()

    def read(self):
        print("test")
        existent_years = self.__session.query(Year).all()
        print(existent_years)
        return existent_years