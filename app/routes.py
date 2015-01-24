from flask import render_template, flash, request, redirect, url_for
from app import app
from .forms import LoginForm, SignupForm

# front-end views

@app.route('/')
@app.route('/index')
@app.route('/home')
def welcome():
    return render_template('index.html', title='Welcome')

@app.route('/todo')
def todo_app():
    return render_template('task-manager.html')

@app.route('/player')
def player_app():
    return render_template('music-player.html')

@app.route('/editor')
def editor_app():
    return render_template('code-editor.html')

@app.route('/users/register', methods=['GET', 'POST'])
def register_form():
    return render_template('users/signup.html', title='Signup')

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

# back-end api routes

@app.route('/api/v1')
def api_welcome():
    return render_template('api/hello.html')

@app.route('/api/v1/users')
def api_users_all():
    return 'All users in storage (as json output)';

@app.route('/api/v1/users/1')
def api_get_user_by_id():
    return 'Specified user in storage (as json output)';

@app.route('/api/v1/users/<username>')
def api_get_user_by_username(username):
    return 'User %s in storage (json output)' % username;