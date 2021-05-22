from selenium import webdriver
from bs4 import BeautifulSoup

topics = [
    # 'smoking+effects',
    # 'drinking+effects',
    'lack+of+exercise+effects'
    ] # Topics should be pass based on user fit

# Falta llamar a main con una variable

def videoRecommendation():
    driver = webdriver.Chrome()
    
    Recommendations = {}

    # Loop through topics of user
    for topic in topics:

        driver.get('https://www.youtube.com/results?search_query={}&sp=CAM%253D'.format(topic))
        content = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content, 'lxml')
        titles = soup.findAll('a', id='video-title')
        views = soup.findAll('span', class_='style-scope ytd-video-meta-block')
        video_urls = soup.findAll('a',id='video-title')

        

        print('\n\nTopic: {}'.format(topic))

        i=0 # index for view & upload date in views
        j=0 # index for video_urls

        for title in titles[:10]:
            print('\n{}\t{}\t{}\thttps://www.youtube.com{}'.format(title.text,views[i].text,views[i+1].text, video_urls[j].get('href')))
            
            Recommendations[v_url] = video_urls[j].get('href')
            Recommendations[v_title] = title.text

            i+=2 # views contain index & upload date, so next set of views got +2 index
            j+=1 # next url
            

    return Recommendations


# BIBLIOGRAPHY: 
# Benjamin Carlson. (5 de junio de 2020). "Web Scraping Popular YouTube Videos | Python One Day Builds". Youtube. https://youtu.be/zhkhdD2hkQw
