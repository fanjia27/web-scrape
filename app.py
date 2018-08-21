# import necessary libraries
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# create instance of Flask app
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# create route that renders index.html template and finds documents from mongo
@app.route("/")
def home():
    # Find data
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)


# Route that will trigger scrape functions
@app.route("/scrape")
def scrape():

    # Run scraped functions
    first = scrape_mars.scrape_first()
    second = scrape_mars.scrape_second()
    third =scrape_mars.scrape_third()
    four = scrape_mars.scrape_four()

    mars_data = {
        "news_title": first["news_title"],
        "news": first["news"],
        "first_img": second["first_img"],
        "weather_today": third["weather_today"],
        "hemisphere_image_urls": four,
    }
    
    # Update the database
    mars = mongo.db.mars
    mars.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
