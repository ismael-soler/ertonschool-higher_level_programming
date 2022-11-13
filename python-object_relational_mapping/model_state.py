#!/usr/bin/python3
""" Creating a table and a database with SQLAlchemy """
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ Model State Class with sqlalchemy """
    __tablename__ = "state"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
