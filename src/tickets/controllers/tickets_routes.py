from tickets import app, db
from tickets.models.models import Tickets, Users
from flask import render_template


@app.route("/all/tickets")
def show_all_tickets():
    tickets_user_data = db.session.query(Tickets, Users).filter(Users.id == Tickets.user_id).all()

    return render_template('tickets.html', tickets=tickets_user_data, bar_included=True)


@app.route("/tickets/<user_id>")
def show_tickets_per_user(user_id):
    tickets = Tickets.query.filter_by(user_id)