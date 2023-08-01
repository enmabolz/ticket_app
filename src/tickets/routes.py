from tickets import app, db
from tickets.models.models import Users, Tickets, EntriesOfTickects
from tickets.models.forms import LoginForm, RegisterForm
from flask import render_template, url_for, redirect, flash
from datetime import datetime

@app.route("/")
def login():
    db.create_all()
    print(str(datetime.now))
    form = LoginForm()
    return render_template("login.html", form=form)

@app.route("/register")
def register_user():
    form = RegisterForm()
    return render_template('register_user.html', form=form)


@app.route("/home/admin")
def home_admin_user():

    record = Tickets(
        number_of_secuence = 1,
        description = "jonjkfnjk kewmfjklfklf ikejkfnjkf",
        enddate = None,
        status = "In Progress",
        duration_in_days = None,
        user_id = 1,
    )

    record1 = Tickets(
        number_of_secuence = 1,
        description = "jonjkfnjk kewmfjklfklf ikejkfnjkf",
        enddate = None,
        status = "In Progress",
        duration_in_days = None,
        user_id = 1,
    )

    db.session.add(record)
    db.session.add(record1)
    db.session.commit()



    tickets_data = Tickets.query.all()
    print(tickets_data)
    return render_template('home_admin.html', tickets=tickets_data)
