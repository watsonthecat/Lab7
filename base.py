from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

#Engine represents the core interface to the database
#The first argument is the url of the database

engine = create_engine('sqlite:///merchManager.db', echo = False)

Base = declarative_base() #All of the mapped classes inherit from this
