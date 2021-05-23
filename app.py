
from operator import ne
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


@app.route('/')
def home():
    return redirect(url_for('main'))

@app.route('/health', methods = ['GET', 'POST'])
def health():
    if request.method == 'POST': # When a user clicks "Calculate" button it will come here
        data = request.form # request the data from the form in health.html file
        first_name = data['first_name']
        last_name = data['last_name']
        birth_year = data['birth_year']
        height = data['height']
        weight = data['weight']
        state = data['state']

        new_data = Users(first_name, last_name, birth_year, height, weight, state)
        db.session.add(new_data)
        db.session.commit()

        user_data = Users.query.all()

        return render_template('health.html', user_data = user_data) # passes user_data variable into the index.html file.
    return render_template('health.html')


if __name__ == '__main__':
    db.create_all
    app.run(debug=True)




