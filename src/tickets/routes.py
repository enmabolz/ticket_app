from tickets import app, db
from tickets.models.models import Users, Tickets, EntriesOfTickects
from tickets.models.forms import LoginForm
from flask import render_template, url_for, redirect, flash

@app.route("/")
def home():
    db.create_all()
    form = LoginForm()
    return render_template("login.html", form=form)
