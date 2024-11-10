from typing import Annotated, Optional

from fastapi import Form
from sqlmodel import Field, SQLModel


class Table(SQLModel, table=True):
    ROWID: Optional[int] = Field(default=None, primary_key=True)
    data: Annotated[str, Form()]
