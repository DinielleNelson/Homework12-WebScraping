from bs4 import BeautifulSoup as bs
import requests

#import selenium
from selenium import webdriver

# # Step 1 - Scraping
# ## NASA Mars News

driver = webdriver.Chrome()

# Import webpage data
url1 = "https://mars.nasa.gov/news/"

driver.get(url1)
html = driver.page_source

soup = bs(html,'html.parser')

# Collect the latest News Title and Paragraph
# Empty lists returned with ('ul', class_="item_list"), ('li', class_="slide")
article_list = soup.body.find_all('div', class_="image_and_description_container")

first_headline = (soup.body.find_all('div', class_="content_title"))[0]
headline = first_headline.a.text.strip()

# Retrieve first article teaser 
first_teaser = (soup.body.find_all('div', class_="article_teaser_body"))[0]
teaser = first_teaser.text


# ## JPL Mars Space Images - Featured Image
from splinter import Browser

executable_path = {'executable_path':'chromedriver.exe'}
browser = Browser('chrome',**executable_path, headless=False)

url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url2)
driver.get(url2)
html2 = driver.page_source
soup2 = bs(html2,'html.parser')

# Index to make a single object not a list, even though there is only one result
retrieval2 = (soup2.body.find_all("div", class_="carousel_items"))[0]
retrieval2b = (soup2.body.find_all("div", class_="carousel_items"))

# split URL out
for div in retrieval2b:
    test=div.find('article')['style']
test = test.split('(\'')[1].split('\')')[0]


#Current url. Perhaps split to retrieve index URL
driver.current_url

featured_image_url = "https://www.jpl.nasa.gov" + test

# Mars Facts
import pandas as pd

url3 = "https://space-facts.com/mars/"
tables = pd.read_html(url3)
df = tables[0]
df.to_html('mars_weather.html')
html_table = df.to_html()
html_table = html_table.replace('\n','')

# ## Mars Hemispheres
from splinter import Browser

executable_path = {'executable_path':'chromedriver.exe'}
browser = Browser('chrome',**executable_path, headless=False)

url4 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url4)
driver.get(url4)
html4 = driver.page_source
soup4 = bs(html4,'html.parser')
print(soup4.prettify())

retrieval4 = soup4.body.find_all('div', class_="description")

# find hyperlinks to click through

# Testing results of loop
link_loop =[]
# Testing results of links found
link_list = []
# Testing results of titles found
title_list = []
# List of dictionaries required by assignment
hemisphere_dicts = []

for each in retrieval4:
    test2 = each.find('a')['href']
    link_loop.append(test2)
    
    url5 = 'https://astrogeology.usgs.gov'+test2
    browser.visit(url5)
    driver.get(url5)
    html5 = driver.page_source
    soup5 = bs(html5,'html.parser')
    test3 = (soup5.body.find('img', class_="wide-image"))['src']
    img_url = 'https://astrogeology.usgs.gov'+test3
    link_list.append(img_url)
    
    hemisphere = soup5.body.find('h2').text.strip()
    hemisphere = hemisphere.split(' Enhanced')[0]
    title_list.append(hemisphere)
    hemisphere_dict = {"title":hemisphere, "img_url":img_url}
    hemisphere_dicts.append(hemisphere_dict)
 

