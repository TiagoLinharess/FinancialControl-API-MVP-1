from models import Session, Year

class YearRepository():

    def __init__(self, session: Session):
        self.__session = session

    def create(self, year_string: str) -> Year:
        existent_year = self.exist_year(year_string)

        if existent_year:
            return existent_year

        year = Year(year_string)
        self.__session.add(year)
        return year

    def read(self) -> [Year]:
        existent_years = self.__session.query(Year).all()
        return existent_years

    def exist_year(self, year_string: str) -> Year:
        existent_years = self.read()

        for year in existent_years:
            if year.year == year_string:
                return year
        
        return