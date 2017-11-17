import ui, merch_orm

# Previous version used handle_choice method to route the user / functionality replaced with Flask

# def handle_choice(choice):
#
#     if choice == '1':
#         show_items()
#
#     elif choice == '2':
#         new_merch()
#
#     elif choice == '3':
#         new_event()
#
#     elif choice == '4':
#         new_sale()
#
#     elif choice == '5':
#         merch_sale_records()
#
#     elif choice == '6':
#         event_sale_records()
#
#     elif choice == '7':
#         delete_merch_item()
#
#     elif choice == '8':
#         delete_event()
#
#     elif choice == '9':
#         delete_sale()
#
#     elif choice == 'q':
#         quit()
#
#     else:
#         ui.message('Please enter a valid selection')

""" delete_merch_item: Takes mid(merchID), then calls merch_orm delete by id function """


def delete_merch_item(mid):

    merch_orm.delete_object_by_id('Merch', mid)


""" delete_event: Takes eid(eventID) and calls merch_orm delete by id """


def delete_event(eid):

    merch_orm.delete_object_by_id('Event', eid)


"""delete_sale: Takes sid(saleID) and calls merch_orm delete by id """


def delete_sale(sid):

    merch_orm.delete_object_by_id('Sale', sid)


"""show_items: Fetch and show all Merch Items"""


def show_items():

    # merch_list is returned from query @ merch_orm
    # that list passed into ui's show_list() to make user friendly
    ui.show_list(merch_orm.merch_list())


"""new_merch: Get info from user, add new Merch Item"""


def new_merch():

    # declares new variable to hold object properties from user input/web form
    new_merch = ui.get_new_merch_info()
    # pass those to add to database function
    merch_orm.add_object_to_db('Merch', new_merch)


"""new_event: Get info from user, add new Event"""


def new_event():

    # declares new variable to hold object properties from user input/web form
    new_event = ui.get_new_event_info()
    # pass those to add to database function
    merch_orm.add_object_to_db('Event', new_event)


"""new_sale: Get info from user, add new Sale"""


def new_sale():

    # declares new variable to hold object properties from user input/web form
    new_sale = ui.get_new_sale_info()
    # pass those to add to database function
    merch_orm.add_object_to_db('Sale', new_sale)


'''merch_sale_records: Get Merch ID # from user, then query for results'''


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

# def event_sale_records():
#     '''Get Event ID # from user, then query for results'''
#     #show list of events for user reference (they probably haven't memorized event ID #'s)
#     event_list = merch_orm.event_list()
#     ui.show_event_list(event_list)
#
#     #get event id from user
#     id = ui.get_id()
#
#
#     merch_orm.sales_by_eventID(id)

# def quit():
#     '''Perform shutdown tasks'''
#     ui.message('Bye!')
#
# def main():
#
#     #setup DB
#     merch_orm.setup()
#
#     quit = 'q'
#     choice = None
#
#     while choice != quit:
#         choice = ui.display_menu_get_choice()
#         handle_choice(choice)
#
# if __name__ == '__main__':
#     main()
