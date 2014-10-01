# import modules to get access to many useful functions :)

# Flask - a lightweight web/backend framework for Python lang
from flask import Flask

app = Flask(__name__)

# create an index page route
@app.route('/')
def hello_world():
    return 'Hello World!'

# run the flask-based app when '__main__' function/method is encountered
if __name__ == '__main__':
    app.run()