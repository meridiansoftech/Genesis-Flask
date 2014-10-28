# import modules to get access to many useful functions :)

# Flask - a lightweight web/backend framework for Python lang
from flask import Flask, render_template

# create Flask instance
app = Flask(__name__)

# index page route
@app.route('/')
@app.route('/index')
@app.route('/home')
def welcome():
    return render_template('index.html')

@app.route('/todo')
def todo_app():
    return render_template('task-manager.html')

@app.route('/player')
def player_app():
    return render_template('music-player.html')

@app.route('/editor')
def editor_app():
    return render_template('code-editor.html')

# run the flask-based app when '__main__' function/method is encountered
if __name__ == '__main__':
    app.run()