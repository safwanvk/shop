from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SECRET_KEY'] = 'ffjdbfdbfjsdgfs43543745'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from admin import routes