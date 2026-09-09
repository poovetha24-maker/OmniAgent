import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is missing from .env")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


def test_connection():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            print("CockroachDB connected successfully!")
            print("Result:", result.scalar())
    except Exception as e:
        print("Database connection failed:")
        print(e)