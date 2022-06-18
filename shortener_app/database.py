# shortener_app/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import get_settings

engine = create_engine("postgresql://ystvatsjikzagi:e0b4e33a0d687506bb6e04fd9f44e0c5efd08215f1c77331db6e227f28462aee@ec2-34-198-186-145.compute-1.amazonaws.com:5432/de6jsbsjhk0gh6", echo=True
)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
