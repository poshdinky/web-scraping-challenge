# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import os


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


#Part  1: Scraping

# ### NASA Mars News
# #### Scrape the Mars News Site and collect the latest News Title and Paragraph Text. *

# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')

slide_elem.find('div', class_='content_title')

# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
print(news_title)

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
print(news_p)


# JPL Mars Space Images—Featured Image
# Save a complete URL string for this image.

# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
print(img_soup)
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
print(img_url)

# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
print(img_url)

# Mars Facts

# use Pandas to scrape the table containing facts about the planet including diameter, mass, etc.
# use Pandas to convert the data to a HTML table string.

df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()

df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df

df.to_html()


#  Mars Hemispheres
# Visit the astrogeology site to obtain high-resolution images for each hemisphere of Mars.

# Save the image URL string for the full resolution hemisphere image and the hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.

# Get Current Path
    
current_path = os.getcwd()

# Create Image Path

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://marshemispheres.com/")

# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'
browser.visit(url)

# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
html = browser.html
hemi_soup = soup(html, 'html.parser')
hemi_links = hemi_soup.find_all('h3')

list_h3 = list()

for i in hemi_links:
    list_h3.append(i.text.strip())

print(list_h3)

list_h3.pop()
print(list_h3)


for image_title in list_h3:
    hemispheres = {}
    url = ""
    
    driver.get("https://marshemispheres.com/")
    link = driver.find_element("link text",image_title)
    link.click()

    for i in driver.find_elements("xpath","//ul/li/a"):
        if i.text.strip() == "Sample":
            url = i.get_attribute("href")

    hemispheres['img_url']   = url
    hemispheres['title']     = image_title
    hemisphere_image_urls.append(hemispheres)
    

print(hemisphere_image_urls)
