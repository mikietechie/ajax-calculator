"""..."""

import typing as tp


from dto import CalculationModel


class CalculatorService:
    """..."""

    @classmethod
    def sanitize(cls, statement: str) -> str:
        """..."""
        return statement

    @classmethod
    def calculate(cls, statement: str) -> str:
        """..."""
        statement = cls.sanitize(statement)
        return str(eval(statement))


class DbService:
    """..."""

    def __init__(self):
        self.calculations: tp.List[CalculationModel] = []

    def select(self, uid: int) -> str:
        """..."""
        return [i for i in self.calculations if i.uid == uid]

    def insert(self, calculation: CalculationModel) -> CalculationModel:
        """..."""
        self.calculations.append(calculation)
        return calculation
