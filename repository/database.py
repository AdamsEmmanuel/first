from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = 'mysql+pymysql://root:ppnaDMzMp5CUR9Sr@localhost:3306/nutrition_therapy_db'  # change to postgres later

engine = create_engine(
    DATABASE_URL
    #connect_args={"check_same_thread": True}  # needed for SQLite
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()