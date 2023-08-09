from tickets import app, db
from tickets.models.models import Tickets, Users, EntriesOfTickects
from tickets.models.forms import CreateTicket
from flask import render_template, redirect, url_for, flash
from flask_login import current_user, login_required


@app.route("/all/tickets", methods=["GET", "POST"])
@login_required
def show_all_tickets():
    tickets_user_data = db.session.query(Tickets, Users).filter(Users.id == Tickets.user_id).all()

    return render_template(
        'tickets.html', 
        tickets=tickets_user_data, 
        bar_included=True, 
        is_admin=current_user.is_admin
    )


@app.route("/create/ticket", methods=["GET", "POST"])
@login_required
def create_ticket():
    form = CreateTicket()
    users = [user[0] for user in Users.query.with_entities(Users.username).all()]
    
    if not users:
         flash("Error!! No user created", category="danger")
         return redirect(url_for('show_all_tickets'))
    
    form.user.choices=users

    if form.validate_on_submit():
        assigned_user_id = Users.query.filter_by(username=form.user.data).first().id

        ticket = Tickets(
            name = form.name.data,
            description = form.description.data,
            user_id = assigned_user_id
        )

        db.session.add(ticket)
        db.session.commit()
        flash(f"Ticket {ticket.name} created", category="success")

        return redirect(url_for('show_all_tickets'))
    
    if form.errors != {}:
        for key, message in form.errors.items():
            flash(f"Error creating ticket: {key}:{message}", category="danger")


    return render_template(
        "create_ticket.html", 
        form=form, 
        bar_included=True, 
        is_admin=current_user.is_admin
    )


@app.route("/ticket/<ticket_id>", methods=["GET", "POST"])
@login_required
def show_ticket_details(ticket_id):
    ticket = Tickets.query.get(ticket_id)

    if ticket:
        user_of_ticket = Users.query.get(ticket.user_id)
        entries_of_ticket = EntriesOfTickects.query.filter_by(ticket_id=ticket_id).all()
    else:
        user_of_ticket = []
        entries_of_ticket = []
    
    return render_template(
        "show_ticket_details.html", 
        ticket=ticket, 
        user_of_ticket=user_of_ticket, 
        entries_of_ticket=entries_of_ticket,
        bar_included=True,
        is_admin = current_user.is_admin
    )
    

@app.route("/tickets/user/<user_id>")
@login_required
def show_tickets_per_user(user_id):
    tickets = Tickets.query.filter_by(user_id=user_id).all()

    return render_template(
        "tickets_per_user.html", 
        tickets=tickets, 
        bar_included=True,
        is_admin=current_user.is_admin
    )


@app.route("/edit/ticket/<ticket_id>")
def edit_ticket(ticket_id):
    pass


    

    



