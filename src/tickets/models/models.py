from tickets import db, bcrypt
from datetime import datetime
 

class Users(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(length=30), nullable=False)
    lastname = db.Column(db.String(length=30), nullable=False)
    birthdate = db.Column(db.DateTime(), nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False)
    email = db.Column(db.String(length=30))
    username = db.Column(db.String(length=50), nullable=False)
    password_hash = db.Column(db.String(length=500), nullable=False)

    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self, plain_password):
        self.password_hash = bcrypt.generate_password_hash(plain_password).decode('utf-8')     
    



class Tickets(db.Model):
    id = db.Column(db.Integer(), nullable=False, primary_key=True, autoincrement=True)
    number_of_secuence = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.String(length=500), nullable=False)
    initialdate = db.Column(db.DateTime, nullable=False, default=datetime.today())
    enddate = db.Column(db.DateTime)
    status = db.Column(db.String(), nullable=False)
    duration_in_days = db.Column(db.Integer())
    user_id = db.Column(db.Integer(), nullable=False)


class EntriesOfTickects(db.Model):
    id = db.Column(db.Integer(), nullable=False, primary_key=True, autoincrement=True)
    number_of_secuence = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    initialdate = db.Column(db.DateTime, nullable=False, default=datetime.today())
    enddate = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(length=50), nullable=False)
    id_ticket = db.Column(db.Integer(), nullable=False)


