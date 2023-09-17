#!/usr/bin/python3
"""Define the City class using SQLAlchemy"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State

class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False
