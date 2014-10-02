# import modules to get access to many useful functions :)

# Flask - a lightweight web/backend framework for Python lang
from flask import Flask, render_template

# create Flask instance
app = Flask(__name__)

# index page route
@app.route('/')
def welcome():
    return render_template('index.html')

# run the flask-based app when '__main__' function/method is encountered
if __name__ == '__main__':
    app.run()