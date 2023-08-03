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

    user1 = Users(
        name = "Enmanuel",
        lastname = "Bolzonello",
        birthdate = datetime.today(),
        is_admin = True,
        email = "enm@gmail.com",
        username = "enmabolz", 
        password = "tejnejenjee888jn",
    )

    user2 = Users(
        name = "Enma",
        lastname = "Bolzo",
        birthdate = datetime.today(),
        is_admin = True,
        email = "enym@gmail.com",
        username = "enmabolz", 
        password = "tejnejenje76888kkl",
    )

    user3 = Users(
        name = "Julio",
        lastname = "Ramirez",
        birthdate = datetime.today(),
        is_admin = True,
        email = "enmt@gmail.com",
        username = "enmabolz", 
        password = "tejnejijkjijiuonjbhjbkkl",
    )

    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.commit()

    return render_template('register_user.html', form=form)


@app.route("/all/tickets")
def show_all_tickets():
    tickets_user_data = db.session.query(Tickets, Users).filter(Users.id == Tickets.user_id).all()

    return render_template('tickets.html', tickets=tickets_user_data, bar_included=True)


@app.route("/tickets/<user_id>")
def show_tickets_per_user(user_id):
    tickets = Tickets.query.filter_by(user_id)


