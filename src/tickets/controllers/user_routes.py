from tickets import app
from tickets.models.forms import RegisterForm, LoginForm, Users
from flask import render_template, flash, redirect, url_for
from tickets import db
from tickets.models.models import Users, Tickets
from flask_login import login_user, current_user, login_required


@app.route("/", methods=["GET", "POST"])
def login():
    db.create_all()
    form = LoginForm()

    if form.validate_on_submit():
        attempted_user = Users.query.filter_by(username=form.username.data).first()
        
        if attempted_user and attempted_user.check_password_correction(form.password.data):
            login_user(attempted_user)
            flash(f"User {attempted_user.username} logged", category="success")
            return redirect(url_for('user_logged'))
        else:
            flash("Wrong username or password", category="danger") 

    if form.errors != {}:
        for key, message in form.errors.items():
            flash(f"Error {key}:{message}", category="danger")           

    return render_template("login.html", form=form)
 

@app.route("/user/logged")
@login_required
def user_logged():
    if current_user.is_admin:
        return redirect(url_for('show_all_tickets'))
    else:
        return redirect(url_for('show_tickets_per_user', user_id=current_user.id))


@app.route("/show/users")
@login_required
def show_users():
    users = Users.query.all()

    return render_template("users.html", users=users, bar_included=True)


@app.route("/register", methods=["GET", "POST"])
@login_required
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
        flash(f"User {user.username} created", category="success")
                
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
        

@app.route("/user/<user_id>", methods=["GET", "POST"])
@login_required
def show_user(user_id):
    user = Users.query.get(user_id)
    tickets = Tickets.query.filter_by(user_id=user_id).all()

    return render_template(
        "user_details.html", 
        user=user, 
        tickets=tickets, 
        bar_included=True
    )