import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

Base = declarative_base()

def session_factory():
    load_dotenv()
    DB_USERNAME = os.getenv('DB_USERNAME')
    DB_PASSWORD = os.getenv('DB_PASSWORD' )
    DB_HOSTNAME = os.getenv('DB_HOSTNAME')
    DB_PORT = os.getenv('DB_PORT')
    DB_DATABASE = os.getenv('DB_DATABASE')

    engine = create_engine(f"mysql+pymysql:{DB_PASSWORD}//{DB_USERNAME}:@{DB_HOSTNAME}:{DB_PORT}/{DB_DATABASE}")
    _SessionFactory = sessionmaker(bind=engine)

    Base.metadata.create_all(engine, checkfirst=True)
    return _SessionFactory()