""" ORM = Object-relational mapping """

from sqlalchemy import create_engine
from sqlalchemy import exc
from sqlalchemy.orm import sessionmaker
from base import Base
from sales import Sale
from events import Event
from merch import Merch
import ui


'''Engine represents the core interface to the database'''

# The first argument is the url of the database;
# echo=True turns on SQLAlchemy logging for debugging

engine = create_engine('sqlite:///merchManager.db', echo = True)

# Base = declarative_base() #All of the mapped classes inherit from this class
Base.metadata.create_all(engine)  # Create a table for all the classes that use Base

'''Need a session to talk to the database'''
# A session manages mappings of objects to rows in the database
# Make a session class -- only need to do this one time
Session = sessionmaker(bind=engine) # using the engine created earlier

""" setup(): Initial database setup, CREATES Merch table and ADDS 3 Merch Objects to db 
    (just so there is something to show initially) """


def setup():
    # Ask the session to instantiate a session object
    # Use the session object to talk to DB
    save_session = Session()

    # Create a merch object; use named args to set values of the object
    item1 = Merch(description = 'Band Shirt', price = 20)
    item2 = Merch(description = 'Band CD', price = 10)
    item3 = Merch(description = 'Sticker/Pin', price = 5)

    for merch in [item1, item2, item3]:
        # if it doesn't already exist
        if not (getItem(merch.description)):
            # Add merch object to session -- this tells the session that you want to map
            # the merch object to a row in the DB
            save_session.add(merch)
            # The merch is pending - not yet saved
            # Doesn't save to DB until session is committed, or closed

    # Commit to save changes
    save_session.commit() # now merch should be saved in DB
    save_session.close()


""" merch_list(): Opens session, query database for all items in Merch table, return results """


def merch_list():

    '''Search Function'''
    search_session = Session()
    # Get a list of merch objects
    all_merch_list = search_session.query(Merch).all()

    return all_merch_list


""" event_list(): Opens session, query database for all items in Events table, return results """


def event_list():
    '''Search Function'''
    search_session = Session()
    # Get a list of event objects
    all_events_list = search_session.query(Event).all()

    return all_events_list


""" sales_list(): Opens session, query database for all items in Sales table, return results"""


def sales_list():

    '''Search Function'''
    search_session = Session()
    # Get a list of event objects
    all_sales_list = search_session.query(Sale).all()

    return all_sales_list


# def show_all():
#
#     '''Search Function'''
#     search_session = Session()
#     # Get a list of event objects
#     all_objects_list = search_session.query(ObType).all()
#
#     return all_objects_list


""" delete_object_by_id(): Opens session, queries database for object id,
    depending on ObjectType, will delete from that table"""


def delete_object_by_id(ObjectType, id):

    # Ask the session to instantiate a session object
    # Use the session object to talk to DB
    save_session = Session()

    item = get_object_by_ID(ObjectType, id)

    if ObjectType == 'Merch':

        save_session.delete(item)
        ui.message('Deleted Merch Item from DB')

    elif ObjectType == 'Event':

        save_session.delete(item)
        ui.message('Deleted Event from DB')

    elif ObjectType == 'Sale':

        save_session.delete(item)
        ui.message('Deleted Sale from Records')

    save_session.commit()
    save_session.close()


""" add_object_to_db(): Opens session, for arguments passed in, it adds to a list
    those are then added to new instantiated object with those parameters and added to DB"""


def add_object_to_db(ObjectType, *args):
    # Ask the session to instantiate a session object
    # Use the session object to talk to DB
    save_session = Session()
    argList = []

    # convert arguments into list
    for arg in args:
        argList.extend(arg)

    if ObjectType == 'Merch':

        merch = Merch(description=argList[0], price=argList[1])
        save_session.add(merch)
        ui.message('Added Merch Item to DB')

    elif ObjectType == 'Event':

        event = Event(venue=argList[0], month=argList[1], day=argList[2], year=argList[3])
        save_session.add(event)
        ui.message('Added Event to DB')

    elif ObjectType == 'Sale':

        sale = Sale(merchID=argList[0], numSold=argList[1], eventID=argList[2])
        save_session.add(sale)
        ui.message('Added Sale to Records')

    save_session.flush()
    save_session.commit()
    save_session.close()


""" get_object_by_ID(): Opens session to talk to DB, queries DB (via ID#) - table to query depending on object type,
    returns the results of query (returns object with id you were looking for)"""


def get_object_by_ID(ObjectType, aid):

    search_session = Session()

    while True:
        if ObjectType == 'Merch':
            try:
                item = search_session.query(Merch).filter_by(id=aid).one()
                break
            except exc.SQLAlchemyError:
                # loops until it gets valid input
                aid = (input('Please enter a Merch ID from the list: '))
        elif ObjectType == 'Event':
            try:
                item = search_session.query(Event).filter_by(id=aid).one()
                break
            except exc.SQLAlchemyError:
                aid = (input('Please enter a Event ID from the list: '))
        elif ObjectType == 'Sale':
            try:
                item = search_session.query(Sale).filter_by(id=aid).one()
                break
            except exc.SQLAlchemyError:
                aid = (input('Please enter a Sale ID from the list: '))

    search_session.close()
    return item


#
# def sales_by_merchID(mid):
#
#     total = 0
#     search_session = Session()
#
#     item = get_object_by_ID('Merch',mid)
#
#     #get all instances of sales that have received id as attribute
#     merchSales = search_session.query(Sale).filter_by(merchID = item.id).all()
#
#     for sale in merchSales:
#         total += sale.numSold * item.price
#
#     print('Total sales for '+item.description+': $'+str(round(total,2)))
#     search_session.close()
#
#
# def sales_by_eventID(eid):
#
#     total = 0
#     search_session = Session()
#
#     event = get_object_by_ID('Event',eid)
#     #get all instances of sales that have received id as attribute
#     eventSales = search_session.query(Sale).filter_by(eventID = event.id).all()
#
#     for sale in eventSales:
#         merch = search_session.query(Merch).filter_by(id = sale.id).one()
#         total += sale.numSold * merch.price
#
#     print('Total sales at '+event.venue+': $'+str(round(total,2)))
#
#     search_session.close()

""" saleTotal(): Function to calculate the total of a sale (Amount Sold + Price of Item) and returns total"""


def saleTotal(sid, mid):

    total = 0
    search_session = Session()
    sale = search_session.query(Sale).filter_by(id=sid).one()
    merchSold = search_session.query(Merch).filter_by(id=mid).one()

    total += sale.numSold * merchSold.price

    return str(round(total, 2))


''' getItem(): Used in database setup returns true if Merch.description is more than 0 characters'''


def getItem(string):

    search_session = Session()
    count = search_session.query(Merch).filter_by(description=string).count()

    if (count > 0):
        search_session.close()
        return True
    else:
        search_session.close()
        return False
