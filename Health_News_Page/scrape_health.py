#importing dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import time
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def scrape():
    #set up splinter 
    executable_path = {"executable_path": "chromedriver.exe"}
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

    #get tha titles of latest 5 news
    latest_news_title1 = latest_news.find_all("a")[1].text
    latest_news_title2 = latest_news.find_all("a")[3].text
    latest_news_title3 = latest_news.find_all("a")[5].text
    latest_news_title4 = latest_news.find_all("a")[7].text
    latest_news_title5 = latest_news.find_all("a")[9].text

    latest_news_title1 = str(latest_news_title1)
    latest_news_title2 = str(latest_news_title2)
    latest_news_title3 = str(latest_news_title3)
    latest_news_title4 = str(latest_news_title4)
    latest_news_title5 = str(latest_news_title5)

    #get the paragraph of the latest 5 news
    news_para1 = latest_news.find_all("p")[0].text
    news_para2 = latest_news.find_all("p")[1].text
    news_para3 = latest_news.find_all("p")[2].text
    news_para4 = latest_news.find_all("p")[3].text
    news_para5 = latest_news.find_all("p")[4].text

    news_para1 = str(news_para1)
    news_para2 = str(news_para2)
    news_para3 = str(news_para3)
    news_para4 = str(news_para4)
    news_para5 = str(news_para5)

    #get the url link of the latest 5 news
    latest_link1 = latest_news.find_all("a", href=True)[0]["href"]
    latest_news_link1 = "https://www.news-medical.net" + latest_link1
    latest_link2 = latest_news.find_all("a", href=True)[2]["href"]
    latest_news_link2 = "https://www.news-medical.net" + latest_link2
    latest_link3 = latest_news.find_all("a", href=True)[4]["href"]
    latest_news_link3 = "https://www.news-medical.net" + latest_link3
    latest_link4 = latest_news.find_all("a", href=True)[6]["href"]
    latest_news_link4 = "https://www.news-medical.net" + latest_link4
    latest_link5 = latest_news.find_all("a", href=True)[8]["href"]
    latest_news_link5 = "https://www.news-medical.net" + latest_link5

    latest_news_link1 = str(latest_news_link1)
    latest_news_link2 = str(latest_news_link2)
    latest_news_link3 = str(latest_news_link3)
    latest_news_link4 = str(latest_news_link4)
    latest_news_link5 = str(latest_news_link5)

    #get the date of the latest 5 news
    latest_Date1 = latest_news.find_all("span", class_="article-meta-date")[0].text
    latest_news_Date1 = latest_Date1.replace('\n', '')
    latest_Date2 = latest_news.find_all("span", class_="article-meta-date")[1].text
    latest_news_Date2 = latest_Date2.replace('\n', '')
    latest_Date3 = latest_news.find_all("span", class_="article-meta-date")[2].text
    latest_news_Date3 = latest_Date3.replace('\n', '')
    latest_Date4 = latest_news.find_all("span", class_="article-meta-date")[3].text
    latest_news_Date4 = latest_Date4.replace('\n', '')
    latest_Date5 = latest_news.find_all("span", class_="article-meta-date")[4].text
    latest_news_Date5 = latest_Date5.replace('\n', '')

    latest_news_Date1 = str(latest_news_Date1)
    latest_news_Date2 = str(latest_news_Date2)
    latest_news_Date3 = str(latest_news_Date3)
    latest_news_Date4 = str(latest_news_Date4)
    latest_news_Date5 = str(latest_news_Date5)

    #get the images of the latest 5 news
    latest_news_image1 = latest_news.find_all("img")[0]["src"]
    latest_news_image2 = latest_news.find_all("img")[1]["src"]
    latest_news_image3 = latest_news.find_all("img")[2]["src"]
    latest_news_image4 = latest_news.find_all("img")[3]["src"]
    latest_news_image5 = latest_news.find_all("img")[4]["src"]

    latest_news_image1 = str(latest_news_image1)
    latest_news_image2 = str(latest_news_image2)
    latest_news_image3 = str(latest_news_image3)
    latest_news_image4 = str(latest_news_image4)
    latest_news_image5 = str(latest_news_image5)
    
    # Closing the browser after scraping
    browser.quit()

    #-------------------------------
    #storing values into directory
    
    health_data = [
        {"title": latest_news_title1, "text": news_para1, "url": latest_news_link1, "date": latest_news_Date1, "image": latest_news_image1},
        {"title": latest_news_title2, "text": news_para2, "url": latest_news_link2, "date": latest_news_Date2, "image": latest_news_image2},
        {"title": latest_news_title3, "text": news_para3, "url": latest_news_link3, "date": latest_news_Date3, "image": latest_news_image3},
        {"title": latest_news_title4, "text": news_para4, "url": latest_news_link4, "date": latest_news_Date4, "image": latest_news_image4},
        {"title": latest_news_title5, "text": news_para5, "url": latest_news_link5, "date": latest_news_Date5, "image": latest_news_image5}
    ]    


    #Return the health_data dict
    return health_data
   



   




