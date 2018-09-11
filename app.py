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

@app.route('/carePackages')
def carePackagesPage():
    return render_template('carePackages.html')

@app.route('/finances')
def financesPage():
    return render_template('finances.html')

@app.route('/makeReceipt')
def makeReceiptPage():
    return render_template('makeReceipt.html')

@app.route('/medicines')
def medicinesPage():
    return render_template('medicines.html')

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


if __name__ == '__main__':
    app.run()
