# -*- coding: utf-8 -*-

import os

from flask import render_template, flash, redirect, url_for, request, g
from flask import send_from_directory
from flask_login import login_user, logout_user, current_user, login_required

from app import app, login_manager , db
#from .forms import LoginForm
from app.models import User, Party
from sqlalchemy import update

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def validateAndAdd(party_name):
    party =  Party.query.filter_by(name=party_name).first()
    party.votes +=  1

@app.route('/', methods=['POST','GET'])
@app.route('/index', methods=['POST', 'GET'])
@login_required
def index():
    if request.method == 'POST':
        pn= request.form['party_name']
        validateAndAdd(pn)
        ########################
        user = User.query.filter_by(id=current_user.id).first()
        user.voted = 1
        db.session.commit()
        return redirect(url_for('login'))
    g.user = current_user #global user parameter used by flask framwork
    parties = Party.query.all()
    return render_template('index.html',
                           title='Home',
                           user=g.user,
                           parties=parties)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':

        ## Validate user
        fn = request.form['first_name']
        ln = request.form['last_name']
        uid = request.form['id']

        user = User.query.filter_by(first_name= fn , last_name=ln , id =uid).first()
        if user:
            if user.voted == 0 :
                login_user(user)  ## built in 'flask login' method that creates a user session
                return redirect(url_for('index'))
            else :
                error =u'המשתמש הנל הצביע כבר'

        else: ##validation error
            error = u'המצביע אינו מופיע בבסיס הנתונים'

    return render_template('login.html',
                           error=error)









## will handle the logout request
@app.route('/logout')
@login_required
def logout():
    logout_user() ## built in 'flask login' method that deletes the user session
    return redirect(url_for('index'))


## secret page that shows the user name
@app.route('/secret', methods=['GET'])
@login_required
def secret():
    return 'This is a secret page. You are logged in as {} {}'.format(current_user.first_name, current_user.last_name)


## will handle the site icon - bonus 2 points for creative new icon
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')
