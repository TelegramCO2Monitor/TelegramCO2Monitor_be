from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class PostgreSQL:
    def __init__(self, user: str, password: str, host: str, port: int, db_name: str):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.db_name = db_name
        self.db_url = f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}"
        self.engine = create_engine(self.db_url)
        self.LocalSession = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)


Base = declarative_base()
