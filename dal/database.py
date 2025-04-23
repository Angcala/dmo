"""
entry point for accessing the database
"""

from tinydb import TinyDB

class Database:
    def __init__(self, database_name: str):
        self.__database_name = database_name

    def get_client(self):
        return TinyDB(self.__database_name)

