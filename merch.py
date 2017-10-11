from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import event
from sqlalchemy.engine import Engine
import sales

from base import Base #All of the mapped classes will use this Base

'''Listen for DB connections to enforce Foreign Key constraints'''
@event.listens_for(Engine, "connect")

def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

class Merch(Base):

    '''Defines metadata about a merch table. Will create Merch objects from rows in this table'''

    __tablename__ = 'merch'

    #Columms: ID, Type, Price
    #These attributes will be column names, and have the types specified

    id = Column(Integer, primary_key=True)
    description = Column(String)
    price = Column(Float)


    def __repr__(self):

        '''Returns string representation of this object, helpful for debugging'''
        #This method gets called when a Merch object is printed

        return 'Merch: Id = {} Description = {} Price = {}'.format(self.id, self.description, self.price)

#update the DB schema to enforce foreign key constraints
engine = create_engine('sqlite:///merchManager.db', echo=False)
Base.metadata.create_all(engine)
