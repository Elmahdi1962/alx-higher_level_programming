#!/usr/bin/python3
'''task 15 model script'''

from relationship_state import State, Base
from sqlalchemy import Column, String, Integer, ForeignKey


class City(Base):
    '''City model for my db'''
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False,
                autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
