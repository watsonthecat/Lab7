from flask import Flask, render_template, request
import merch_orm
import choiceManager
import ui


app = Flask(__name__)

# __name__ helps determine root path

# routing/mapping url to whatever web page you want to connect (return value)
# @ signifies a decorator - way to wrap a function and modifying it's behavior


'''Homepage'''


@app.route('/', methods=['get', 'post'])
def index():
    merchItems = merch_orm.merch_list()
    saleItems = merch_orm.sales_list()
    eventList = merch_orm.event_list()

    if request.method == 'POST':

        try:
            choiceManager.new_merch()

        except RuntimeError as e:
            return render_template(error_text=e.args[0])

    return render_template("index.html", merchItems=merchItems, saleItems=saleItems, eventList=eventList)


'''Sale Management Page'''


@app.route('/sales')
def sales():


    totalsList = []

    saleItems = merch_orm.sales_list()

    for item in saleItems:

        totalsList.append(merch_orm.saleTotal(item.id, item.merchID))

    return render_template("sales.html", saleItems=saleItems, totalsList=totalsList)


@app.route('/merch')
def merch():

    merchItems = merch_orm.merch_list()

    return render_template("merch.html", merchItems=merchItems)
#
#

#
# @app.route('/events')
# def events():
#
#     eventList = merch_orm.event_list()
#     return render_template("events.html", eventList=eventList)


if __name__ == '__main__':

    # setup DB
    merch_orm.setup()

    app.run(debug=True)
    # start this app

