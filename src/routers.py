"""...."""

import time
import datetime
import typing as tp

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


from dto import CalculateReqDto, CalculateResDto, CalculationModel
from services import CalculatorService, DbService

router = APIRouter()
templates = Jinja2Templates(directory="templates")
db = DbService()


@router.get("/", response_class=HTMLResponse)
def index(request: Request):
    """..."""
    return templates.TemplateResponse("index.html", {"request": request})


@router.post("/calculate", response_model=CalculateResDto)
def calculate(body: CalculateReqDto):
    """.."""
    ans = CalculatorService.calculate(body.statement)
    _id = int(str(time.time()).replace(".", ""))
    db.insert(
        CalculationModel(
            uid=0,
            id=_id,
            statement=body.statement,
            ans=ans,
            timestamp=str(datetime.datetime.now()),
        )
    )
    return CalculateResDto(statement=body.statement, ans=ans)


@router.get("/calculations", response_model=tp.List[CalculationModel])
def calculations():
    """.."""
    return db.select(uid=0)
