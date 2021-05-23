
from flask import Flask
from config import key
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

db_url = f'postgresql://postgres:{key}@localhost:5432/health_db'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False #to supress warning
db = SQLAlchemy(app)

#declaring user_habits model

class Users(db.Model):
    id = db.Column(db.Integer, primary_ket = True)
    first_name = db.Column(db.String(80), index = True, unique = False)
    last_name = db.Column(db.String(80), index = True, unique = False)
    birth_year = db.Column(db.Integer, index = True, unique = False)
    id_sex = db.Column(db.String, db.ForeignKey('sex.id'))
    height = db.Column(db.Integer, index = True, unique = False)
    weight = db.Column(db.Integer, index = True, unique = False)
    state = db.Column(db.String, index = True, unique = False)
    id_user_habit = db.Column(db.Integer, db.ForeignKey('habits.id'))
    id_user_evaluation = db.Column(db.Integer, db.ForeignKey('user_evaluation.id'))
    id_user_disease = db.Column(db.Integer, db.ForeignKey('diseases.id'))

class Habits(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    habit_eval_date = db.Column(db.Date, index = True, unique = False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    id_habit = db.Column(db.Integer, db.ForeignKey('habits.id'))
    frequency = db.Column(db.String, index = True, unique = False)




@app.route('/')
@app.route('/home')
def home():
    return 'Nicely done!'

if __name__ == "__main__":
    app.run()




