from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///:memory:", echo=True)
Base = declarative_base()


def get_db_session():
    Base.metadata.create_all(bind=engine)
    return sessionmaker(bind=engine)()
