#!usr/bin/env python3

import os
from flask import Flask, render_template, redirect, url_for, request, flash
from wtforms import Form, TextField, StringField, BooleanField, PasswordField, fields, validators
import model

app = Flask(__name__)
app.config['SECRET_KEY'] = '9876543210'

@app.route('/')
def show_homepage():
    return render_template('index.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('my_page'))
    return render_template('admin.html', error=error)

class Register(Form):
    username = StringField('Username : ', [validators.DataRequired()])
    password = PasswordField('Password : ', [validators.DataRequired()])

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = Register(request.form)
    if request.method == 'POST':
        if form.validate() == True:
            flash('Thanks for registering')
            return redirect(url_for('show_account'))
        else:
            flash('All fields are required')
            return render_template('registration.html', form=form)
    elif request.method == 'GET':
        return render_template('registration.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'aki' or request.form['password'] != 'india':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('show_account'))
    return render_template('login.html', error=error)

@app.route('/account', methods=['GET', 'POST'])
def show_account():
    if request.method == 'POST':
        return render_template('my_page.html')
    elif request.method == 'GET':
        return render_template('account.html')

@app.route('/my_page')
def my_page():
    return render_template('my_page.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
