import sys

import os
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template, session
from werkzeug.utils import secure_filename

from flask import render_template, redirect, url_for, request
from sqlite3 import *
import pymysql
import re

from flask import Flask, jsonify, request
import json, os, signal
import sqlite3

from flask_bcrypt import Bcrypt

from application import app, db
from application.models import Movies, Review, Accounts
from application.forms import MoviesForm, ReviewForm, AccountsForm

bcrypt = Bcrypt(app)

class Routes():
    
    id_num = Movies().id
    id_num = str(id_num)

    @app.route('/')
        

    @app.route('/login', methods =['GET', 'POST'])
    def login():
        msg = ''
        if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
            username  = request.form['username']
            password = request.form['password']
            password = str(password)
            query = 'SELECT password from Accounts WHERE username=?'
            connection = sqlite3.connect('movies.db')
            cursor = connection.cursor()
            c = cursor
            my_result = c.execute(query, (username,))
            row = my_result.fetchone()
            my_password = row[0]
            is_valid = bcrypt.check_password_hash(my_password, password)
            if is_valid:
                new_password = my_password
                cursor.execute('SELECT * FROM Accounts WHERE username = ? AND password = ?', (username, new_password, ))
                account = cursor.fetchone()
                if account:
                    session['loggedin'] = True
                    msg = 'Logged in successfully !'
                    return render_template('index.html', msg = msg)
                else:
                    msg = 'Incorrect username / password !'
        return render_template('login.html', msg = msg)

    @app.route('/user', methods=['GET', 'POST'])
    def user():
        all_movies = Movies.query.all()
        return render_template('movie_index.html', all_movies=all_movies)
        
    
    @app.route('/logout', methods=['GET', 'POST'] )
    def logout():
        session.pop('loggedin', None)
        session.pop('id', None)
        session.pop('username', None)
        return redirect(url_for('login'))
    
    @app.route('/register', methods =['GET', 'POST'])
    def register():
        msg = ''
        if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
            username = request.form['username']
            password = request.form['password']
            password = str(password)
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            connection = sqlite3.connect('movies.db')
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Accounts WHERE username = ?", (username, ))
            account = cursor.fetchone()
            if account:
                msg = 'Account already exists !'
            # elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            #     msg = 'Invalid email address !'
            elif not re.match(r'[A-Za-z0-9]+', username):
                msg = 'Username must contain only characters and numbers !'
            elif not username or not password:
                msg = 'Please fill out the form !'
            else:
                cursor.execute('INSERT INTO Accounts (username, password) VALUES (?, ?)', (username, hashed_password, ))
                connection.commit()
                msg = 'You have successfully registered !'
        elif request.method == 'POST':
            msg = 'Please fill out the form !'
        return render_template('register.html', msg = msg)


    @app.route('/add', methods=['GET', 'POST'])
    def add():
        form = MoviesForm()
        if form.validate_on_submit():
            new_movie = Movies(name=form.name.data)
            db.session.add(new_movie)
            db.session.commit()
            return redirect(url_for('movie_index'))
        return render_template('add.html', form=form)
    
    

    @app.route('/update/<int:idnum>', methods=['GET', 'POST'])
    def update(idnum):
        form = MoviesForm()
        movies_update = Movies.query.get(idnum)
        if form.validate_on_submit():
            movies_update.name = form.name.data
            db.session.commit()
            return redirect(url_for('movie_index'))
        return render_template('update.html', form=form)

    @app.route('/delete/<int:idnum>')
    def delete(idnum):
        movies_delete = Movies.query.get(idnum)
        db.session.delete(movies_delete)
        db.session.commit()
        return redirect(url_for('movie_index'))

    @app.route('/add_review/<int:idnum>', methods=['GET', 'POST'])
    def add_review(idnum):
        form = ReviewForm()
        if form.validate_on_submit():
            new_review = Review(rev=form.rev.data, rating=form.rating.data, movies_id=idnum)
            db.session.add(new_review)
            db.session.commit()
            return redirect(url_for('reviews', idnum=idnum))
        return render_template('add_review.html', form=form, movies=Movies.query.get(idnum))

    @app.route('/reviews/<int:idnum>', methods=['GET', 'POST'])
    def reviews(idnum):
        reviews = Review.query.filter_by(movies_id=idnum).all()
        return render_template ('reviews.html', reviews=reviews)

