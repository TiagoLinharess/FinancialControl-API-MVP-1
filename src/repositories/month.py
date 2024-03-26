from models import Session, Year, Month

class MonthRepository():
    months = ["januar", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]

    def __init__(self, session: Session):
        self.__session = session

    def create(self, month_string: str, year: Year) -> Month:
        existent_month = self.exist_month(month_string, year)

        if not self.is_valid(month_string):
            raise ValueError("Month is not valid.")

        if existent_month:
            raise ValueError("Month already added.")

        month = Month(month_string)
        year.add_month(month)
        return month
    
    def read(self, year: Year) -> [Month]:
        months = self.__session.query(Month).filter(Month.year == year.id).all()
        return months
    
    def exist_month(self, month_string: str, year: Year) -> Month:
        existent_months = self.read(year)

        for month in existent_months:
            if month.month == month_string:
                return month
        
        return

    def is_valid(self, month_string: str) -> bool:
        if month_string in self.months: 
            return True
        else:
            return False