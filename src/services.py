"""..."""

import typing as tp


from dto import CalculationModel


class CalculatorService:
    """..."""

    @classmethod
    def sanitize(cls, statement: str) -> str:
        """..."""
        sanitized = ""
        safe = ".0123456789()-+/* "
        for char in statement:
            if char in safe:
                sanitized = sanitized + char
        return sanitized

    @classmethod
    def calculate(cls, statement: str) -> str:
        """..."""
        statement = cls.sanitize(statement)
        try:
            return str(eval(statement, {}, {}))
        except Exception:
            return "Error"


class DbService:
    """..."""

    def __init__(self):
        self.calculations: tp.List[CalculationModel] = []

    def select(self, uid: int) -> str:
        """..."""
        return [i for i in self.calculations if i.uid == uid][::-1]

    def insert(self, calculation: CalculationModel) -> CalculationModel:
        """..."""
        self.calculations.append(calculation)
        return calculation
