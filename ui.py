import merch_orm, choiceManager
from sales import Sale
from merch import Merch
import merch
from events import Event
from flask import request

def display_menu_get_choice():

    '''Display choices for user, return users' selection'''

    print('''
        1. Show list of all Merch items
        2. Add new Merch Item
        3. Add new event/show
        4. Record new sale
        5. Sales Records of Merch items
        6. Sales Records of Events
        7. Delete Merch Item
        8. Delete Event/Show
        9. Delete Sale
        q. Quit
    ''' )

    choice = input('Enter your selection: ')

    return choice

def show_list(merchItems):
    '''Format and display a list of merch objects'''

    if len(merchItems) == 0:
        print ('* No Items in DB *')
        return

    merchItems.sort(key = lambda merch: merch.id) #this sorts the merch items by description(type)

    for merch in merchItems:
        print(merch)

    print('* {} merch item(s) *'.format(len(merchItems)))

def show_event_list(eventList):
    '''Format and display list of Events'''

    if len(eventList) == 0:
        print('* No Events in DB *')
        return

    #eventList.sort(key = lambda event: event.id) #this sorts the merch items by description(type)

    for event in eventList:
        print(event)

    print('* {} event(s) *'.format(len(eventList)))

def show_sales_list(salesList):
    '''Format and display list of sales'''
    if len(salesList) == 0:
        print('* No Events in DB *')
        return

    for sale in salesList:
        print(sale)

    print('* {} sale(s) *'.format(len(salesList)))



def get_new_merch_info():
    '''Get Description and Price of Merch Item from user'''

    description = request.form.get('description')
    price = request.form.get('price')


    return (description,price)

def get_new_event_info():
    '''Get Venue, Day, Month & Year of New Event from user'''

    venue = request.form.get('venue')
    month = request.form.get('month')
    day = request.form.get('day')
    year = request.form.get('year')

    return (venue,month,day,year)

def get_new_sale_info():

    merchID = request.form.get('merchID')
    numSold = request.form.get('numSold')
    eventID = request.form.get('eventID')

    return (merchID,numSold,eventID)

def get_id():

    id = input('Enter ID to Search Records: ')

    return id


def message(msg):
    '''Display a message to the user'''
    print(msg)
