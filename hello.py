# import modules to get access to many useful functions :)

# Flask - a lightweight web/backend framework for Python lang
from flask import Flask
from flask import render_template

app = Flask(__name__)

# index page route
@app.route('/')
def hello_world():
    return 'Hello World!'

# index template render route
@app.route('/html')
def templates(name=None):
    return render_template('index.html', name=name)

# user profile route
# @app.route('/user')
# show_user()

# run the flask-based app when '__main__' function/method is encountered
if __name__ == '__main__':
    app.run()