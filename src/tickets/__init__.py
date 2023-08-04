from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///tickets.db"
app.config['SECRET_KEY'] = 'ec9439cfc6c796ae2029594d'
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

import tickets.controllers.user_routes
import tickets.controllers.tickets_routes





