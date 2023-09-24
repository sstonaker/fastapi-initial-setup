from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLITE_URL = (
    "sqlite:///database.db"
)

# The argument connect_args={"check_same_thread": False}
# ...is needed only for SQLite. It's not needed for other databases.
engine = create_engine(SQLITE_URL, echo=True, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
