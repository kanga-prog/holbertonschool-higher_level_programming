#!/usr/bin/python3

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base

class City(Base):
    """Définition de la classe City, liée à la table cities"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

