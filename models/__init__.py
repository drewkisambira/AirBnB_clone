#!/usr/bin/python3
"""
create a uniq FileStorage instance for your application
"""


from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()