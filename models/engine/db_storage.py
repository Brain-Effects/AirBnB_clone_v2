#!/usr/bin/python3
"""
Contains the class DBStorage
"""

from models.base_model import BaseModel, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from os import getenv


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        USER = getenv('HBNB_MYSQL_USER')
        PWD = getenv('HBNB_MYSQL_PWD')
        HOST = getenv('HBNB_MYSQL_HOST')
        DB = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(USER, PWD, HOST, DB), pool_pre_ping=True)

    def all(self, cls=None):
        """Query on the current database session"""
        # Implementation of querying logic based on cls
        pass

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and the current database session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Call remove() method on the private session attribute"""
        self.__session.remove()


if __name__ == "__main__":
    storage = DBStorage()
    storage.reload()
