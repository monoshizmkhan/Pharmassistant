from flask import *

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
    medList=[None]*10000
    a = "123Napa*Napa*Paracetamol*30*5*01-01-2020"
    b = "456Ace*Ace*Paracetamol*40*3*01-01-2020"
    medList[0]=a
    medList[1]=b
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

@app.route('/medicines/ace')
def aPage():
    return render_template('Ace.html')

@app.route('/medicines/napa')
def bPage():
    return render_template('Napa.html')


if __name__ == '__main__':
    app.run()
