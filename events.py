from sqlalchemy import Column, Integer, String, create_engine
from base import Base



class Event(Base):

    __tablename__ = 'events'

    id = Column(Integer, primary_key = True)
    venue = Column(String)
    month = Column(Integer)
    day = Column(Integer)
    year = Column(Integer)


    def __repr__(self):

        return 'Event ID: {} Venue: {} Date: {}-{}-{}'.format(self.id, self.venue, self.month, self.day, self.year)


# updates the db schema to enforce foreign key constraints
engine = create_engine('sqlite:///merchManager.db', echo=False)
Base.metadata.create_all(engine)

