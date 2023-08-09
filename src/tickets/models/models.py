from tickets import db, bcrypt
from datetime import datetime
from flask_login import UserMixin
from tickets import login_manager


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))
 

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(length=30), nullable=False)
    lastname = db.Column(db.String(length=30), nullable=False)
    birthdate = db.Column(db.DateTime(), nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    email = db.Column(db.String(length=30))
    username = db.Column(db.String(length=50), nullable=False)
    password_hash = db.Column(db.String(length=500), nullable=False)

    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self, plain_password):
        self.password_hash = bcrypt.generate_password_hash(plain_password).decode('utf-8')   


    def check_password_correction(self, attemped_password):
        return bcrypt.check_password_hash(self.password_hash, attemped_password)  
    

class Tickets(db.Model):
    id = db.Column(db.Integer(), nullable=False, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(length=500), nullable=False)
    initialdate = db.Column(db.DateTime, nullable=False, default=datetime.today())
    enddate = db.Column(db.DateTime)
    status = db.Column(db.String(), nullable=False, default="Created")
    duration_in_days = db.Column(db.Integer())
    user_id = db.Column(db.Integer(), nullable=False)


class EntriesOfTickects(db.Model):
    id = db.Column(db.Integer(), nullable=False, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    initialdate = db.Column(db.DateTime, nullable=False, default=datetime.today())
    enddate = db.Column(db.DateTime)
    status = db.Column(db.String(length=50), nullable=False, default="Created")
    duration_in_days = db.Column(db.Integer())
    ticket_id = db.Column(db.Integer(), nullable=False)
    


