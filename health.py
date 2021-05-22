from selenium import webdriver
from bs4 import BeautifulSoup
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import videoRecommendation

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/health_app"
mongo = PyMongo(app)

@app.route("/")
def index():
    Recommendations = mongo.db.Recommendations.find_one()
    return render_template("index.html", Recommendations=Recommendations)

# Falta llamar a main con una variable
@app.route("/videoRecommendation")
def v_recommendation():
    Recommendations = mongo.db.Recommendations
    Recommendations_data = videoRecommendation.videoRecommendation()
    Recommendations.update({}, Recommendations_data, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)