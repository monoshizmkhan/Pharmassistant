from flask import *
from Classes.Utilities import Iterator
from Classes.DatabaseAccessors import AccessDatabaseMedicines as adm
from Classes import Statics

app = Flask(__name__)


@app.route('/')
def startupPage():
    accountList=Statics.accounts
    return render_template('signInPage.html', accountList=accountList)

@app.route('/home')
def homepage():
    usr=Statics.currentUser
    return render_template('homepage.html', usr=usr)

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
    a = Iterator.Iterator
    a = adm.AccessDatabaseMedicines().getIterator()
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
    manageSearch = Iterator.Iterator
    manageSearch = adm.AccessDatabaseMedicines().getIterator()
    Statics.searchResult=manageSearch.search(Statics.searchKey)
    #Statics.searchResult="No matches"
    if Statics.searchResult=="":
        Statics.searchResult="No Matches"
    return render_template('searchResults.html', searched = Statics.searchResult)


@app.route('/searchHandler', methods=['POST'])
def search():
    searchRequest = request.get_json(force=True)
    for i in searchRequest:
        Statics.searchKey += str(i['queried'])

@app.route('/updateUser', methods=['POST'])
def update():
    currentUser = request.get_json(force=True)
    for i in currentUser:
        Statics.currentUser+=str(i['current'])

if __name__ == '__main__':
    app.run()
