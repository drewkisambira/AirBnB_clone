#!/usr/bin/python3


from models.engine.file_storage import FileStorage
from importlib import reload

storage = FileStorage()
storage.reload()