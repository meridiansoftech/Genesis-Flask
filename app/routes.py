from flask import render_template, request, redirect, url_for
from app import app

# index page route
@app.route('/')
@app.route('/index')
@app.route('/home')
def welcome():
    return render_template('index.html', title='Genesis for Flask')

@app.route('/todo')
def todo_app():
    return render_template('task-manager.html')

@app.route('/player')
def player_app():
    return render_template('music-player.html')

@app.route('/editor')
def editor_app():
    return render_template('code-editor.html')