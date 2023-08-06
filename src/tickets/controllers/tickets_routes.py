from tickets import app, db
from tickets.models.models import Tickets, Users
from tickets.models.forms import CreateTicket
from flask import render_template, redirect, url_for, flash


@app.route("/all/tickets")
def show_all_tickets():
    tickets_user_data = db.session.query(Tickets, Users).filter(Users.id == Tickets.user_id).all()

    return render_template('tickets.html', tickets=tickets_user_data, bar_included=True)


@app.route("/create/ticket", methods=["GET", "POST"])
def create_ticket():
    form = CreateTicket()
    users = [user[0] for user in Users.query.with_entities(Users.username).all()]
    form.user.choices=users

    if form.validate_on_submit():
        last_number_of_secuence = Tickets.query.with_entities(Tickets.number_of_secuence).order_by(Tickets.number_of_secuence.desc()).first()[0]
        assigned_user_id = Users.query.filter_by(username=form.user.data).first().id

        ticket = Tickets(
            number_of_secuence = last_number_of_secuence + 1,
            description = form.description.data,
            user_id = assigned_user_id
        )

        db.session.add(ticket)
        db.session.commit()

        return redirect(url_for('show_all_tickets'))
    
    if form.errors != {}:
        for key, message in form.errors.items():
            flash(f"Error creating ticket: {key}:{message}", category="danger")


    return render_template('create_ticket.html', form=form, bar_included=True)



@app.route("/tickets/<user_id>")
def show_tickets_per_user(user_id):
    tickets = Tickets.query.filter_by(user_id)
    





    



