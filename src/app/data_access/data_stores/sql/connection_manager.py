from typing import Any
from pyodbc import connect
from app.core.constants.sql_drivers import POSTGRESQL as driver

class ConnectionManager(object):

    def __init__(self, 
    host: str, 
    database: str, 
    username: str, 
    password: str) -> None:
        self.__host: str = host
        self.__database: str = database
        self.__username: str = username
        self.__password: str = password

    def get_connection(self) -> Any:
        connection_string: str = f'DRIVER={driver};SERVER={self.__host};DATABASE={self.__database};UID={self.__username};PWD={self.__password}'
        
        return connect(connection_string)
