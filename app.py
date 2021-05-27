from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_health

<<<<<<< HEAD
#create an instance of Flask
app = Flask(__name__)
=======
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

    #Function to pass user's data and gets as new entry in the table
    def __init__(self, first_name, last_name, birth_year, height, weight, state):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.height = height
        self.weight = weight
        self.state = state

>>>>>>> 3fd363de8aedf85414c0a06c196842ce18b7ffb5

#Use Pymongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/health_app")

#delete in production
mongo.db.collection.drop()

#route to render index.html template using data from mongo
@app.route("/")
def news_and_recommendations():

<<<<<<< HEAD
    #find one record of data from mongo database
    health_data = mongo.db.health_data.find_one()
    
    #return template and data
    return render_template("news_and_recommendations.html", health_data=health_data)
    
#route that will trigger the scrape function
@app.route("/scrape")
def scrape():


    health = mongo.db.health_data
    health_data = scrape_health.scrape()
    #health.insert_many(health_data)
    health.update({}, health_data, upsert=True)

    print(health_data)
=======
    return render_template('health.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
>>>>>>> 3fd363de8aedf85414c0a06c196842ce18b7ffb5

    return redirect("/", code=302)
    
if __name__ == "__main__":
    app.run(debug=True)     



