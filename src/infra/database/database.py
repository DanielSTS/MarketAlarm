from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from src.infra.database.models import Base

engine = create_engine("sqlite:///:memory:", echo=True)
Base.metadata.create_all(bind=engine)
session = sessionmaker(bind=engine)()
