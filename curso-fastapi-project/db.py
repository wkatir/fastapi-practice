from typing import Annotated
from fastapi import Depends
from sqlmodel import Session, create_engine

sqilite_name = "db.sqlite3"
sqlite_url = f"sqlite:///{sqilite_name}"

engine = create_engine(sqlite_url)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]


