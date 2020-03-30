#!/usr/bin/python3
""" This module defines a class 'City' """

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """ This is a class that defines a city. """

    """====================================================================="""
    """=================== INIT & CLASS VARIABLES =========================="""
    """====================================================================="""
    __tablename__ = 'cities'

    id = Column(Integer, autoincrement="auto", unique=True,
                primary_key=True, nullable=False)

    name = Column(String(128), nullable=False)

    state_id = Column(Integer, ForeignKey('states_id'), nullable=False)
