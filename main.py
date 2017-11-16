from flask import Flask, render_template, request, redirect
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


@app.route('/delStuff', methods=['POST'])
def del_stuff():
    merch_id = request.form.get('merch-id')
    event_id = request.form.get('event-id')
    sale_id = request.form.get('sale-id')

    if not merch_id is None:
        pass
    if not event_id is None:
        pass
    if not sale_id is None:
        pass

    if request.method == 'POST':
        if request.form['submit'] == 'del_merch_btn':
            choiceManager.delete_merch_item(merch_id)
        elif request.form['submit'] == 'event-id':
            choiceManager.delete_event(event_id)
        elif request.form['submit'] == 'sale-id':
            choiceManager.delete_sale(sale_id)
        else:
            pass  # unknown

    # choiceManager.delete_merch_item(merch_id)
    # choiceManager.delete_event(event_id)
    # choiceManager.delete_sale(sale_id)

    return redirect("/dostuff")


'''Make changes to existing Records '''


@app.route('/dostuff', methods=['GET', 'POST'])
def editor():

    totalsList = []

    if request.method == 'POST':
        if request.form['submit'] == 'new_merch_btn':
            choiceManager.new_merch()
        elif request.form['submit'] == 'new_event_btn':
            choiceManager.new_event()
        elif request.form['submit'] == 'new_sale_btn':
            choiceManager.new_sale()
        else:
            pass  # unknown

    merchItems = merch_orm.merch_list()
    saleItems = merch_orm.sales_list()
    eventList = merch_orm.event_list()

    for item in saleItems:

        totalsList.append(merch_orm.saleTotal(item.id, item.merchID))

    return render_template("editor.html", merchItems=merchItems, saleItems=saleItems, eventList=eventList
                               ,totalsList=totalsList)


if __name__ == '__main__':

    # setup DB
    merch_orm.setup()

    app.run(debug=True)
    # start this app

