
from flask import Flask
from sqlalchemy.orm import backref
from config import key
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask import Flask , render_template, jsonify, request, redirect, url_for, jsonify

db_url = f'postgresql://postgres:{key}@localhost:5432/health_db'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False #to supress warning
db = SQLAlchemy(app)

#declaring models to create tables in database

class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(80), index = True, unique = False)
    last_name = db.Column(db.String(80), index = True, unique = False)
    birth_year = db.Column(db.Integer, index = True, unique = False)
    height = db.Column(db.Integer, index = True, unique = False)
    weight = db.Column(db.Integer, index = True, unique = False)
    state = db.Column(db.String, index = True, unique = False)
    user_habits = db.relationship('UserHabits', backref = 'users', lazy='dynamic')

class UserHabits(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    frequency = db.Column(db.String, index = True, unique = False)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    





app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('index'))

@app.route('/health', methods = ['GET', 'POST'])



if __name__ == "__main__":
    app.run()




