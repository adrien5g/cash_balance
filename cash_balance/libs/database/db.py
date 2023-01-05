from typing import List
from sqlmodel import Session

from .connection.database_handler import Database

db = Database()

def get_session() -> List[Session]:
    with db as session:
        yield session
