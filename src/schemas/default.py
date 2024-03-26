class DefaultRequestSchema():

    # Inicializa request
    def __init__(self, year: str, month: str):
        self.__year = year
        self.__month = month
    
    # Busca valor de YEAR
    def get_year(self) -> str:
        return self.__year
    
    # Busca valor de MONTH
    def get_month(self) -> str:
        return self.__month