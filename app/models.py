
from database import Base
from sqlalchemy import Column, Integer, Text


class Table(Base):
    __tablename__ = "table"

    ROWID = Column(Integer, primary_key=True)
    data = Column(Text)
