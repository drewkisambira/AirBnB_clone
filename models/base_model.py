#!/usr/bin/python3
""" project base class
"""


from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    define base class
    """

    def __init__(self):

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return "[{:s}] ({:s}) {:s}".format(
            self.__class__.__name__, self.id, str(self.__dict__))

    def save(self):
        """method that updates updated_at with current datetime
        """

        self.updated_at = datetime.now()

    def to_dict(self):

        new_dict = self.__dict__.copy()
        new_dict.update(__class__=self.__class__.__name__)
        new_dict.update(created_at=self.created_at.isoformat())
        new_dict.update(updated_at=self.updated_at.isoformat())

        return new_dict
