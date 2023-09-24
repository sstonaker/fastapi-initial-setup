import models
from sqlalchemy.orm import Session


def get_all_records(db: Session):
    return db.query(models.Table).all()


def get_record_by_rowid(db: Session, ROWID: int):
    return db.query(models.Table).filter(models.Table.ROWID == ROWID).first()


def create_record(db: Session, record: models.Table):
    db.add(record)
    db.commit()
    db.refresh(record)
    return record


def update_record(db: Session, record: models.Table):
    db_record = db.get(models.Table, record.ROWID)
    record_dict = record.dict(exclude_unset=True)
    for k, v in record_dict.items():
        setattr(db_record, k, v)
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record
