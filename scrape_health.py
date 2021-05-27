#importing dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import time
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def scrape():
    #set up splinter 
<<<<<<< HEAD
    #executable_path = {"executable_path": ChromeDriverManager().install()}
    executable_path = {"executable_path": "chromedriver.exe"}
=======
    executable_path = {"executable_path": ChromeDriverManager().install()}
    #executable_path = {"executable_path": "chromedriver.exe"}
>>>>>>> 3fd363de8aedf85414c0a06c196842ce18b7ffb5
    browser = Browser("chrome", **executable_path, headless=False)

    #--------------------------
    #News Medical Life Sciences

    #visit
    url = "https://www.news-medical.net/condition/Metabolic-Syndrome"
    browser.visit(url)
    time.sleep(1)

    #scrape page into soup
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    # Retrieve all elements that contain news
    latest_news = soup.find("div", class_="posts publishables-list-wrap")

    #latest news titles-----------------------
    latest_news_title = []

    #get tha titles of latest 5 news
    latest_news_title1 = latest_news.find_all("a")[1].text
    latest_news_title1 = str(latest_news_title1)
    latest_news_title.append({"news_title": latest_news_title1})

    latest_news_title2 = latest_news.find_all("a")[3].text
    latest_news_title2 = str(latest_news_title2)
    latest_news_title.append({"news_title": latest_news_title2})

    latest_news_title3 = latest_news.find_all("a")[5].text
    latest_news_title3 = str(latest_news_title3)
    latest_news_title.append({"news_title": latest_news_title3})
    
    #latest news paragraph--------------------
    latest_news_para = [] 

    #get the paragraph of the latest 5 news
    news_para1 = latest_news.find_all("p")[0].text
    news_para1 = str(news_para1)
    latest_news_para.append({"news_para": news_para1})

    news_para2 = latest_news.find_all("p")[1].text
    news_para2 = str(news_para2)
    latest_news_para.append({"news_para": news_para2})

    news_para3 = latest_news.find_all("p")[2].text
    news_para3 = str(news_para3)
    latest_news_para.append({"news_para": news_para3})
    
    #latest news links-----------------------
    latest_news_link = []

    #get the url link of the latest 5 news
    latest_link1 = latest_news.find_all("a", href=True)[0]["href"]
    latest_news_link1 = "https://www.news-medical.net" + latest_link1
    latest_news_link1 = str(latest_news_link1)
    latest_news_link.append({"news_link": latest_news_link1})

    latest_link2 = latest_news.find_all("a", href=True)[2]["href"]
    latest_news_link2 = "https://www.news-medical.net" + latest_link2
    latest_news_link2 = str(latest_news_link2)
    latest_news_link.append({"news_link": latest_news_link2})

    latest_link3 = latest_news.find_all("a", href=True)[4]["href"]
    latest_news_link3 = "https://www.news-medical.net" + latest_link3
    latest_news_link3 = str(latest_news_link3)
    latest_news_link.append({"news_link": latest_news_link3})

    #latest news dates-----------------------
    latest_news_date = []

    #get the date of the latest 5 news
    latest_Date1 = latest_news.find_all("span", class_="article-meta-date")[0].text
    latest_news_Date1 = latest_Date1.replace('\n', '')
    latest_news_Date1 = str(latest_news_Date1)
    latest_news_date.append({"news_date": latest_news_Date1})

    latest_Date2 = latest_news.find_all("span", class_="article-meta-date")[1].text
    latest_news_Date2 = latest_Date2.replace('\n', '')
    latest_news_date2 = str(latest_news_Date2)
    latest_news_date.append({"news_date": latest_news_date2})

    latest_Date3 = latest_news.find_all("span", class_="article-meta-date")[2].text
    latest_news_Date3 = latest_Date3.replace('\n', '')
    latest_news_date3 = str(latest_news_Date3)
    latest_news_date.append({"news_date": latest_news_date3})

    #latest news images-----------------------
    latest_news_image = []

    #get the images of the latest 5 news
    latest_news_image1 = latest_news.find_all("img")[0]["src"]
    latest_news_image1 = str(latest_news_image1)
    latest_news_image.append({"news_image": latest_news_image1})

    latest_news_image2 = latest_news.find_all("img")[1]["src"]
    latest_news_image2 = str(latest_news_image2)
    latest_news_image.append({"news_image": latest_news_image2})

    latest_news_image3 = latest_news.find_all("img")[2]["src"]
    latest_news_image3 = str(latest_news_image3)
    latest_news_image.append({"news_image": latest_news_image3})

    # Closing the browser after scraping
    browser.quit()

    #-------------------------------
    #storing values into directory
    
    health_data = {
        "title": latest_news_title,
        "para": latest_news_para,
        "link": latest_news_link,
        "date": latest_news_date,
        "image": latest_news_image
    }
    
    #Return the health_data dict
    return health_data
  



   




