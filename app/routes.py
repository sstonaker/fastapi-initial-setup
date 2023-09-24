import crud
import schemas
import utils
from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

router = APIRouter()

templates = Jinja2Templates(directory="templates")
templates.env.globals["get_flashed_messages"] = utils.get_flashed_messages


@router.get("/")
def index(
    request: Request,
    db: Session = Depends(utils.get_db),
):
    try:
        data = crud.get_all_records(db)
    except Exception as e:
        utils.flash(
            request, f"Unable to retrieve data from database. {e}", "alert-danger"
        )
        return templates.TemplateResponse("error.html", {"request": request})

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "data": data,
        },
    )


@router.get("/data/{ROWID}", response_model=schemas.Table)
def data(
    request: Request,
    ROWID: int,
    db: Session = Depends(utils.get_db),
):
    try:
        data = crud.get_record_by_rowid(db, ROWID)
    except TypeError as e:
        raise HTTPException(
            status_code=400, detail=f"Invalid id - must be integer-like. {e}"
        )
    if not data:
        raise HTTPException(
            status_code=502, detail=f"Data (id:{ROWID}) not found."
        )

    return templates.TemplateResponse(
        "data.html",
        {
            "request": request,
            "data": data,
        },
    )
