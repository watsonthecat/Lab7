from flask import Flask, render_template, request
import merch_orm
import choiceManager



app = Flask(__name__)

# __name__ helps determine root path

# routing/mapping url to whatever web page you want to connect (return value)
# @ signifies a decorator - way to wrap a function and modifying it's behavior


'''Homepage'''


@app.route('/', methods=['get', 'post'])
def index():


    return render_template("index.html")


'''Sale Management Page'''


@app.route('/sales')
def sales():


    totalsList = []

    saleItems = merch_orm.sales_list()

    for item in saleItems:

        totalsList.append(merch_orm.saleTotal(item.id, item.merchID))

    return render_template("sales.html", saleItems=saleItems, totalsList=totalsList)

''' Merch Management Page '''

@app.route('/merch')
def merch():

    merchItems = merch_orm.merch_list()

    return render_template("merch.html", merchItems=merchItems)


''' Events Manager Page'''
@app.route('/events')
def events():

    eventList = merch_orm.event_list()

    return render_template("events.html", eventList=eventList)


'''Make changes to existing Records '''

@app.route('/dostuff', methods=['GET', 'POST'])
def editor():
    merchItems = merch_orm.merch_list()
    saleItems = merch_orm.sales_list()
    eventList = merch_orm.event_list()

    totalsList = []

    for item in saleItems:

        totalsList.append(merch_orm.saleTotal(item.id, item.merchID))

    if request.method == 'POST':
        if request.form['submit'] == 'new_merch_btn':
            choiceManager.new_merch()
        elif request.form['submit'] == 'new_event_btn':
            choiceManager.new_event()
        elif request.form['submit'] == 'new_sale_btn':
            choiceManager.new_sale()
        else:
            pass  # unknown
    elif request.method == 'GET':

        return render_template("editor.html", merchItems=merchItems, saleItems=saleItems, eventList=eventList,
                               totalsList=totalsList)




if __name__ == '__main__':

    # setup DB
    merch_orm.setup()

    app.run(debug=True)
    # start this app

