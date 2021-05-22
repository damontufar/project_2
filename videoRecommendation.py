from selenium import webdriver
from bs4 import BeautifulSoup

topics = [
    'smoking+effects',
    'drinking+effects',
    'lack+of+exercise+effects'
    ] # Topics should be pass based on user fit

Recommendations = {
    'v_url': [],
    'v_title': [],
    'v_topic': []
    }

# Falta llamar a main con una variable

def videoRecommendation():
    driver = webdriver.Chrome() 

    # Loop through topics of user
    for topic in topics:

        driver.get('https://www.youtube.com/results?search_query={}&sp=CAM%253D'.format(topic))
        content = driver.page_source.encode('utf-8').strip()

        # Scrape page into Soup
        soup = BeautifulSoup(content, 'lxml')

        # Find elements
        # views = soup.findAll('span', class_='style-scope ytd-video-meta-block') # contain index & upload date, so next element of views is view+2
        video_urls = soup.findAll('a',id='video-title')

        # Store data in a dictionary
        Recommendations['v_url'].append(['https://www.youtube.com' + url.get("href") for url in video_urls])
        Recommendations['v_title'].append([url.text for url in video_urls])
        Recommendations['v_topic'].append(topic)

        # Print to terminal - Testing.............
        # print('\n\nTopic: {}'.format(topic))
        # i=0 # index for view & upload date in views
        # j=0 # index for video_urls
        # for title in titles[:10]:
        #     print('\n{}\t{}\t{}\thttps://www.youtube.com{}'.format(title.text,views[i].text,views[i+1].text, video_urls[j].get('href')))
        #     i+=2 # views contain index & upload date, so next set of views got +2 index
        #     j+=1 # next url
        # print(Recommendations)

    return Recommendations

# BIBLIOGRAPHY: 
# Benjamin Carlson. (5 de junio de 2020). "Web Scraping Popular YouTube Videos | Python One Day Builds". Youtube. https://youtu.be/zhkhdD2hkQw