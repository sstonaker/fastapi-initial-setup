from typing import Annotated

import crud
import models
import utils
from fastapi import APIRouter, Depends, Form, HTTPException, Request, status
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

router = APIRouter()

templates = Jinja2Templates(directory="templates")
templates.env.globals["get_flashed_messages"] = utils.get_flashed_messages


@router.get("/")
def index(
    request: Request,
    db: Session = Depends(utils.get_db),
):
    try:
        records = crud.get_all_records(db)
    except Exception as e:
        utils.flash(
            request, f"Unable to retrieve record from database. {e}", "alert-danger"
        )
        return templates.TemplateResponse("error.html", {"request": request})

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "records": records,
        },
    )


@router.get("/record/{ROWID}")
def read(
    request: Request,
    ROWID: int,
    db: Session = Depends(utils.get_db),
):
    try:
        record = crud.get_record_by_rowid(db, ROWID)
    except TypeError as e:
        raise HTTPException(
            status_code=400, detail=f"Invalid id - must be integer-like. {e}"
        )
    if not record:
        raise HTTPException(
            status_code=502, detail=f"Record (id:{ROWID}) not found."
        )

    return templates.TemplateResponse(
        "record.html",
        {
            "request": request,
            "record": record,
        },
    )


@router.get("/record")
def add_record(
    request: Request
):
    return templates.TemplateResponse(
        "record.html",
        {
            "request": request,
        },
    )


@router.post("/record")
async def create(
    request: Request,
    form_data: Annotated[str, Form()],
    db: Session = Depends(utils.get_db),
):
    print("Test")
    record = models.Table(data=form_data)

    try:
        crud.create_record(db, record)
    except Exception as e:
        raise HTTPException(
            status_code=502, detail=f"Unable to add record. {e}"
        )

    utils.flash(
        request, "New record added.", "alert-success"
    )

    # status code must be changed since by default redirect (307) preserves the
    # request type - index as "GET" will not accept redirect with "POST" from this route
    return RedirectResponse(
        url=request.url_for("index"), status_code=status.HTTP_303_SEE_OTHER
    )


@router.post("/record/{ROWID}")
async def update(
    request: Request,
    ROWID: int,
    form_data: Annotated[str, Form()],
    db: Session = Depends(utils.get_db),
):
    record = models.Table(ROWID=ROWID, data=form_data)
    try:
        crud.update_record(db, record)
    except Exception as e:
        raise HTTPException(
            status_code=502, detail=f"Unable to add record. {e}"
        )

    utils.flash(
        request, "Record updated.", "alert-success"
    )

    # status code must be changed since by default redirect (307) preserves the
    # request type - index as "GET" will not accept redirect with "POST" from this route
    return RedirectResponse(
        url=request.url_for("index"), status_code=status.HTTP_303_SEE_OTHER
    )
