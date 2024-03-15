#!/usr/bin/python3

"""First state model"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, MetaData

myMetaData = MetaData()
Base = declarative_base(metadata=myMetaData)


class State(Base):
    """ class definition of a State and an
    instance Base = declarative_base()"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True,
                nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    