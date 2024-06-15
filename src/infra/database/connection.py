from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker

engine = create_engine("sqlite:///:memory:", echo=True)
Base = declarative_base()
db_session = scoped_session(sessionmaker(bind=engine))
Base.metadata.create_all(bind=engine)
