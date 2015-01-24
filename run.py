#!flask/bin/python

from app import app

# run the flask-based app when '__main__' function/method is encountered
if __name__ == '__main__':
	app.run(debug=True)