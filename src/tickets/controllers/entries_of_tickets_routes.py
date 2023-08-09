from tickets import app, db
from flask import render_template, redirect, url_for
from tickets.models.forms import CreateEntryOfTicket 
from tickets.models.models import EntriesOfTickects
from tickets.models.models import Users, Tickets
from flask_login import current_user


@app.route("/create/entry/<ticket_id>", methods=["GET", "POST"])
def create_entry(ticket_id):
    form = CreateEntryOfTicket()

    if form.validate_on_submit():
        entry = EntriesOfTickects(
            name = form.name.data,
            description = form.description.data,
            ticket_id = ticket_id,
        )

        db.session.add(entry)
        db.session.commit()

        return redirect(url_for('show_ticket_details', ticket_id=ticket_id))

    return render_template(
        "create_entry.html", 
        ticket_id=ticket_id, 
        form=form, 
        bar_included=True,
        is_admin=current_user.is_admin
    )
