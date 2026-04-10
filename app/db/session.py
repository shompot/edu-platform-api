from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:dbaccess1234@localhost/edu_platform"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)