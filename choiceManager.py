import ui, sqlite3, merch_orm
from merch import Merch
from events import Event
from sales import Sale


def handle_choice(choice):

    if choice == '1':
        show_items()

    elif choice == '2':
        new_merch()

    elif choice == '3':
        new_event()

    elif choice == '4':
        new_sale()

    elif choice == '5':
        merch_sale_records()

    elif choice == '6':
        event_sale_records()

    elif choice == '7':
        delete_merch_item()

    elif choice == '8':
        delete_event()

    elif choice == '9':
        delete_sale()

    elif choice == 'q':
        quit()

    else:
        ui.message('Please enter a valid selection')


def delete_merch_item():
    '''Show all Merch Items'''
    show_items()
    '''Get info from user, delete merch item'''
    id = int(input('Enter ID of Merch Item you want to delete: '))
    #TODO: Delete this record
    merch_orm.delete_object_by_id('Merch',id)


def delete_event():
    '''Show all events'''
    #show list of events for user reference (they probably haven't memorized event ID #'s)
    event_list = merch_orm.event_list()
    ui.show_event_list(event_list)
    '''Get info from user, delete event record'''
    id = int(input('Enter ID of event/show you want to delete:'))
    #TODO: Delete this record
    merch_orm.delete_object_by_id('Event',id)

def delete_sale():
    #show list of merch items for user reference (they probably haven't memorized merch ID #'s)
    merch_list = merch_orm.merch_list()
    ui.show_list(merch_list)
    #show list of events for user reference (they probably haven't memorized event ID #'s)
    event_list = merch_orm.event_list()
    ui.show_event_list(event_list)
    #show list of sales for user reference
    sales_list = merch_orm.sales_list()
    ui.show_sales_list(sales_list)
    '''Get info from user, delete sale record'''
    #get sale ID to delete
    id = int(input('Enter ID of the Sale Record you want to delete: '))
    #TODO: Delete this sale ID from db
    merch_orm.delete_object_by_id('Sale',id)


def show_items():
    '''Fetch and show all Merch Items'''
    #TODO:this might not work

    #merch_list is returned from query @ merch_orm
    #that list passed into ui's show_list() to make user friendly
    ui.show_list(merch_orm.merch_list())



def new_merch():
    '''Get info from user, add new Merch Item'''

    new_merch = ui.get_new_merch_info()
    merch_orm.add_object_to_db('Merch', new_merch)

def new_event():
    '''Get info from user, add new Event'''
    new_event = ui.get_new_event_info()
    merch_orm.add_object_to_db('Event', new_event)

def new_sale():
    '''Get info from user, add new Sale'''

    new_sale = ui.get_new_sale_info()
    merch_orm.add_object_to_db('Sale', new_sale)

def merch_sale_records():
    '''Get Merch ID # from user, then query for results'''
    #show list of merch items for user reference (they probably haven't memorized merch ID #'s)
    merch_list = merch_orm.merch_list()
    ui.show_list(merch_list)

    #show list of sales for user reference
    sales_list = merch_orm.sales_list()
    ui.show_sales_list(sales_list)

    #get merch id from user
    print('To get total sales for a specific Merch item, enter Merch ID below:')
    id = ui.get_id()

    #query db for sales information based on Merch ID #
    merch_orm.sales_by_merchID(id)

def event_sale_records():
    '''Get Event ID # from user, then query for results'''
    #show list of events for user reference (they probably haven't memorized event ID #'s)
    event_list = merch_orm.event_list()
    ui.show_event_list(event_list)

    #get event id from user
    id = ui.get_id()

    #TODO query db for sales information based on Event ID #
    merch_orm.sales_by_eventID(id)

def quit():
    '''Perform shutdown tasks'''
    ui.message('Bye!')

def main():

    #setup DB
    merch_orm.setup()

    quit = 'q'
    choice = None

    while choice != quit:
        choice = ui.display_menu_get_choice()
        handle_choice(choice)

if __name__ == '__main__':
    main()
