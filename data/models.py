import os
from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


class Event(Base):
    __tablename__ = 'event'
    event_id = Column(Integer, primary_key=True)
    email_subject = Column(String(250), nullable=False)
    email_body = Column(String(250), nullable=False)
    send_date = Column(TIMESTAMP(timezone=True), nullable=False)


# Create an engine that stores data in the local directory's
# example.db file.
dirname = os.path.dirname(__file__)
path = os.path.join(dirname, 'example.db')
print('dirname', dirname)
print('path', path)
engine = create_engine('sqlite:///{}'.format(path))

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)
