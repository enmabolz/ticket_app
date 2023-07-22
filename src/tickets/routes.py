from tickets import app, db
from tickets.models.models import Users, Tickets, EntriesOfTickects
from tickets.models.forms import LoginForm, RegisterForm
from flask import render_template, url_for, redirect, flash

@app.route("/")
def login():
    db.create_all()
    form = LoginForm()
    return render_template("login.html", form=form)

@app.route("/register")
def register_user():
    form = RegisterForm()
    return render_template('register_user.html', form=form)