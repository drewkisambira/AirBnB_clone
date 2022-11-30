#!/usr/bin/python3
""" project base class
"""


from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """
    define base class
    """

    def __init__(self, *args, **kwargs):
        """
        defining constructor
        """

        if kwargs:
            for k, v in kwargs.items():
                if k == 'created_at' or k == 'updated_at':
                    val = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, k, val)
                elif k != '__class__':
                    setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        method torepresent calss objects as a string
        """

        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, str(self.__dict__))

    def save(self):
        """method that updates updated_at with current datetime
        """

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        method returns a dictionary containing key/values of __dict__
        """

        new_dict = self.__dict__.copy()
        new_dict.update(__class__=self.__class__.__name__)
        new_dict.update(created_at=self.created_at.isoformat())
        new_dict.update(updated_at=self.updated_at.isoformat())

        return new_dict
