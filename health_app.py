
from flask import Flask
from config import key
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, redirect
from os import environ

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('main.html')

@app.route('/health')
def health_form():
    return render_template('health.html')



if __name__ == '__main__':
    app.run(debug=True)