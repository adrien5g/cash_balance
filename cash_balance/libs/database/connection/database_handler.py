from sqlmodel import create_engine, Session
from sqlalchemy.future import Engine

from conf import get_config
from interfaces import Database

class Database(Database):
    
    def __init__(self):
        config = get_config()
        self.session = None
        if config.DB_TYPE == 'sqlserver':
            connection_string = f'sqlite:///{config.DB_HOST}'
        else:
            database_host = f'{config.DB_HOST}:{config.DB_PORT}:{config.DB_DATABASE}'
            database_auth = f'{config.DB_USER}:{config.DB_PASSWORD}'
            connection_string = f'{config.DB_TYPE}://{database_auth}@{database_host}'
        self.engine = create_engine(connection_string)

    def get_engine(self) -> Engine:
        return self.engine

    def get_session(self) -> Session:
        return self.session

    def __enter__(self) -> Session:
        self.session = Session(self.engine)
        return self.session

    def __exit__(self, *args, **kwargs) -> None:
        self.session.close()