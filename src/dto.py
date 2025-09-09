"""..."""

from pydantic import BaseModel


class CalculateReqDto(BaseModel):
    """..."""

    statement: str


class CalculateResDto(BaseModel):
    """..."""

    statement: str
    ans: str


class CalculationModel(BaseModel):
    """..."""

    uid: int
    id: int
    statement: str
    ans: str
    timestamp: str
