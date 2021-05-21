from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_health

#create an instance of Flask
app = Flask(__name__)

#Use Pymongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/health_app")

#delete in production
mongo.db.collection.drop()

#route to render index.html template using data from mongo
@app.route("/")
def index():

    #find one record of data from mongo database
    health_data = mongo.db.health_data.find_one()
    
    #return template and data
    return render_template("index.html", health_data=health_data)
    
#route that will trigger the scrape function
@app.route("/scrape")
def scrape():


    health = mongo.db.health_data
    health_data = scrape_health.scrape()
    health.insert_many(health_data)

    print(health_data)

    return redirect("/", code=302)
    
if __name__ == "__main__":
    app.run(debug=True)     



