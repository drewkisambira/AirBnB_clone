#!/usr/bin/python3
""" project base class
"""


import uuid
from datetime import datetime


class BaseModel:
    """
    define base class
    """

    def __init__(self, *args, **kwargs):

        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'id':
                    value == self.id
                if key == 'created_at':
                    value == self.created_at
                if key == 'updated_at':
                    value == self.updated_at
                
    def __str__(self):
        return "[{:s}] ({:s}) {:s}".format(
            self.__class__.__name__, self.id, str(self.__dict__))

    def save(self):
        """method that updates updated_at with current datetime
        """

        self.updated_at = datetime.today()

    def to_dict(self):
        for k, v in self.__dict__.items():
            return {'__class__': self.__class__.__name__,
                    'updated_at': self.updated_at.isoformat(), 'id': self.id,
                    'created_at': self.created_at.isoformat()}
