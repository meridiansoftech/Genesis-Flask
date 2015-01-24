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

from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

# back-end api routes
@app.route('/api/v1')

def api_welcome():
    return 'Welcome to the LocPay API';

# api feature: user accounts
@app.route('/api/v1/users')

def api_users_all():
    return 'All users in storage (json output)';

@app.route('/api/v1/users/1')

def api_get_user_by_id():
    return 'Specified user in storage (json output)';

@app.route('/api/v1/users/<username>')

def api_get_user_by_username(username):
    return 'User %s in storage (json output)' % username;

# front-end views
@app.route('/')
@app.route('/index')

def index():
    user = {'username': 'jim'}  # fake user
    posts = [  # array of app features
        { 
            'feature': 'user account management', 
            'description': 'The application gives you the flexibility to Create, Update or Delete a user account.' 
        },
        { 
            'feature': 'user profile management', 
            'description': 'Create a profile for your user account. Share your profile with friends.' 
        }
    ]
    return render_template('home.html', user=user, posts=posts)

@app.route('/users/register', methods=['GET', 'POST'])

def register_form():
    return render_template('users/register.html', title='Register')

@app.route('/users/login', methods=['GET', 'POST'])

def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/')
    return render_template('users/login.html', title='Login to ', form=form, providers=app.config['OPENID_PROVIDERS'])


@app.route('/users/me/update')

def update():
    return render_template('users/update.html', title='Update your account')

@app.route('/users/me/delete')

def delete():
    return render_template('users/delete.html', title='Delete your account')
