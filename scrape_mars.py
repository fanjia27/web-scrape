from splinter import Browser
from bs4 import BeautifulSoup as bs
import requests
import pymongo
from selenium import webdriver

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "C:/Users/lovel/Downloads/USCLOS201805DATA1-Class-Repository-DATA-master1/USCLOS201805DATA1-Class-Repository-DATA-master/01-Class-Content/13-Web-Scraping-and-Document-Databases/3/Activities/10-Stu_Scrape_Weather/Solved/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

# Scrape the news title and news contents
def scrape_first():
    browser = init_browser()
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    html = browser.html
    news_soup = bs(html, 'html.parser')
    slide_elem = news_soup.select_one('ul.item_list li.slide')

    slide_elem.find("div", class_='content_title')

    news_title = slide_elem.find("div", class_='content_title')
    mars_news_title = news_title.get_text()

    list_text = slide_elem.find("div", class_='list_text')
    title = list_text.find("div", class_='content_title')
    title.get_text()
    teaser = list_text.find("div", class_='article_teaser_body')
    mars_news= teaser.get_text()
    
    first = {
        "news_title": mars_news_title,
        "news": mars_news,
    }

    return first

# scrape the featured image
def scrape_second():
    browser = init_browser()

    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    html = browser.html
    soup = bs(html, 'html.parser')
    image = soup.find("img", class_="thumb")["src"]
    img_url = "https://jpl.nasa.gov"+image
    featured_image_url = img_url
    
    second = {
        "first_img": featured_image_url,
    }

    return second


# scrape today's weather
def scrape_third():
    browser = init_browser()
    url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url)

    html = browser.html
    weather = bs(html, 'html.parser')
    weather_data = weather.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")
    
    weather_today = weather_data.get_text()
    
    third = {
        "weather_today": weather_today,
    }

    return third

# scrape full resultion images
def scrape_four():
    
    four = [
        {"title": "Cerberus Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/cfa62af2557222a02478f1fcd781d445_cerberus_enhanced.tif_full.jpg"},
        {"title": "Schiaparelli Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/3cdd1cbf5e0813bba925c9030d13b62e_schiaparelli_enhanced.tif_full.jpg"},
        {"title": "Syrtis Major Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/ae209b4e408bb6c3e67b6af38168cf28_syrtis_major_enhanced.tif_full.jpg"},
        {"title": "Valles Marineris Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/7cf2da4bf549ed01c17f206327be4db7_valles_marineris_enhanced.tif_full.jpg"},
    ]

    return four