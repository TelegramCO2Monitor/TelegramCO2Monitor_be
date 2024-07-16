import os
from dotenv import load_dotenv
from src.repositories.PostgreSQL import PostgreSQL, Base
from src.repositories.TelegramBot import TelegramBot

load_dotenv()


def get_config():
    config = {}
    items = os.environ.items()
    for item in items:
        config[item[0]] = item[1]
    config['init'] = config.get('SECRET_CACHE', '1') == '1'
    return config


config = get_config()

db = PostgreSQL(
    user=config['POSTGRES_USER'],
    password=config['POSTGRES_PASSWORD'],
    host=config['POSTGRES_HOST'],
    port=config['POSTGRES_PORT'],
    db_name=config['POSTGRES_DB']
)
SessionLocal = db.LocalSession
engine = db.engine


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    Base.metadata.create_all(bind=engine)


init_db()

telegram_bot = TelegramBot(
    token=config['BOT_TOKEN'],
    db_instance=db
)
