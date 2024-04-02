from pydantic import BaseModel
from typing import List

class ExampleErrorSchema(BaseModel):
    error: str = "Ocorreu um erro"

class ExampleSuccessSchema(BaseModel):
    success: bool = True

class ExampleDeleteSchema(BaseModel):
    id: int

class ExamplePutSchema(BaseModel):
    id: int
    type: str
    name: str
    value: float

class ExamplePostSchema(BaseModel):
    year: str
    month: str
    type: str
    name: str
    value: float

class ExampleIncomeSchema(BaseModel):
    id: int = 1
    name: str = "Bill"
    type: str = "income"
    value: float = 100

class ExampleOutcomeSchema(BaseModel):
    id: int = 2
    name: str = "Bill"
    type: str = "outcome"
    value: float = 100

class ExampleMonthSchema(BaseModel):
    id: int = 1
    month: str = "april"
    incomes: List[ExampleIncomeSchema]
    outcomes: List[ExampleOutcomeSchema]

class ExampleYearSchema(BaseModel):
    year: str = "2024"
    id: int = 1
    months: List[ExampleMonthSchema]

class ExampleYearsListSchema(BaseModel):
    years: List[ExampleYearSchema]
