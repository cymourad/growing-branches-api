# this model represents a servant table in the DB

from sqlalchemy import Column, String, Integer


class Servant(Base):
    __username__ = "servants"

    id = Column(Integer, primary_key=True)
    username = Column(String)
