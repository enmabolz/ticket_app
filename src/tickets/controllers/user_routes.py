from tickets import app
from tickets.models.forms import RegisterForm, LoginForm, Users
from flask import render_template, flash, redirect, url_for
from datetime import datetime
from tickets import db


@app.route("/")
def login():
    db.create_all()
    print(str(datetime.now))
    form = LoginForm()
    return render_template("login.html", form=form)


@app.route("/show/users")
def show_users():
    users = Users.query.all()

    return render_template("users.html", users=users, bar_included=True)


@app.route("/register", methods=["GET", "POST"])
def register_user():
    form = RegisterForm()

    if form.validate_on_submit():
        user = Users(
            name = form.name.data,
            lastname = form.lastname.data,
            birthdate = form.birthdate.data,
            is_admin = form.is_admin.data,
            email = form.email.data,
            username = create_username(form.name.data, form.lastname.data),
            password = form.password.data,
        )
    
        db.session.add(user)
        db.session.commit()
                
        return redirect(url_for('show_users'))
    
    if form.errors != {}:
        for key, message in form.errors.items():
            flash(f'Error creating user: {message}: {key}', category='danger')

    
    return render_template('register_user.html', form=form, bar_included=True)

    
def create_username(name, lastname):
    attempted_user = f'{name.lower().replace(" ", "")}.{lastname.lower().replace(" ", "")}'
    contador = -1

    while True:
        if Users.query.filter_by(username=attempted_user).first():
            contador += 1
            attempted_user = f'{name.lower()}.{lastname.lower()}{contador}'
        else:
            break
    
    return attempted_user
        
