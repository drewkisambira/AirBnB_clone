#!/usr/bin/python3
""" module creates BaseModel class that defines all
common attributes for other classes
"""


import uuid
import datetime


class BaseModel:
    def __init__(self, created_at=0, updated_at=0, id=uuid.uuid4()):
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self):
        return "[BaseModel] ({}) {}".format(self.id, self.__dict__)

    def save(self):
        """define method that updates updated_at with current datetime
        """

        updated_at = datetime.date()
        return updated_at

    def to_dict(self):
        return self.__dict__
