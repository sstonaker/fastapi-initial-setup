import models
from sqlalchemy.orm import Session


def get_all_records(db: Session):
    return db.query(models.Table).all()


def get_record_by_rowid(db: Session, ROWID: int):
    return db.query(models.Table).filter(models.Table.ROWID == ROWID).first()
