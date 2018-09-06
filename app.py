from flask import *

app = Flask(__name__)


@app.route('/')
def startupPage():
    return render_template('signInPage.html')

@app.route('/home')
def homepage():
    tests = "napa"
    tests2 = "ace"
    return render_template('homepage.html', tests=tests, tests2=tests2)

@app.route('/aboutUs')
def aboutUsPage():
    return render_template('aboutUsPage.html')


@app.route('/medicines/napa')
def napaPage():
    return render_template('napa.html')

@app.route('/medicines/ace')
def acePage():
    return render_template('ace.html')


if __name__ == '__main__':
    app.run()
