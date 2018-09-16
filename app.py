from flask import *
from Classes.Utilities import Container, Iterator
from Classes import AccessDatabaseMedicines as adm

app = Flask(__name__)


@app.route('/')
def startupPage():
    return render_template('signInPage.html')

@app.route('/home')
def homepage():
    return render_template('homepage.html')

@app.route('/aboutUs')
def aboutUsPage():
    return render_template('aboutUsPage.html')

@app.route('/finances')
def financesPage():
    return render_template('finances.html')

@app.route('/makeReceipt')
def makeReceiptPage():
    return render_template('makeReceipt.html')

@app.route('/medicines')
def medicinesPage():
    medList=[]
    a = adm.AccessDatabaseMedicines()
    while a.hasNext():
        medList.append(a.next())
    return render_template('medicines.html', medList=medList)

@app.route('/notifications')
def notificationsPage():
    return render_template('notificationsPage.html')

@app.route('/orders')
def ordersPage():
    return render_template('orders.html')

@app.route('/orders/placeOrder')
def placeOrderPage():
    return render_template('placeOrder.html')

@app.route('/accounts')
def accountsPage():
    return render_template('accounts.html')

@app.route('/searchResults')
def resultsPage():
    manageSearch = adm.AccessDatabaseMedicines()
    adm.result=manageSearch.search(adm.searchKey)
    if adm.result=="":
        adm.result="No Matches Found"
    return render_template('searchResults.html', searched = adm.result)


@app.route('/searchHandler', methods=['POST'])
def search():
    searchRequest = request.get_json(force=True)
    for i in searchRequest:
        adm.searchKey += str(i['queried'])

if __name__ == '__main__':
    app.run()
