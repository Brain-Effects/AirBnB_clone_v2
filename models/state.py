#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class State(BaseModel):
    """ State class """
    name = ""

    @property
    def cities(self):
        """Returns the list of City objects linked to the current State"""
        return [city for city in models.storage.all(City).values()
                if city.state_id == self.id]
