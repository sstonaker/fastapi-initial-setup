from pydantic import BaseModel


class Table(BaseModel):
    ROWID: int
    data: str

    class Config:
        orm_mode = True
