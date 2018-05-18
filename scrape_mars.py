import pandas as pd
from bs4 import BeautifulSoup as bs
from splinter import Browser
#from splinter.exceptions import ElementDoesNotExist
import requests
import os
import time
#SETTING UP SPLINTER. USED TO DATA SCRAPE FROM: Astrogeology.usgs.gov 
#executable_path = {"executable_path": "chromedriver.exe"}
#browser = Browser("chrome", **executable_path, headless=False)

def scrape_f():
    print("SCRAPING FOR DATA...............................")
    print("CONTINUING SCRAPING ACTIVITIES..........")
    print("..................................")
    print("......................")
    print("...........")
    print(".......")
    print("...")


    #Inititiate Mars Dict
    marsDict={}
    ###############################################################################
    ###############  Scraping ... Scaping NASA Mars SIte  #########################
    ######################### for latest article ###################################

    #URL Identified. 
    #url = 'https://mars.nasa.gov/news/'
    url='https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'

    #retrieving page and parse html
    # import pdb; pdb.set_trace()

    response = requests.get(url)
    soup = bs(response.text, 'lxml')
    results = soup.find_all('ul', class_="item_list")
    articles =soup.find("div",class_="image_and_description_container")

    # Retrieved news Title and Descrtiption
    news_p=articles.find("div", class_="rollover_description_inner").text
    newsTitle =soup.find("div", class_="content_title").text

    #print(newsTitle)
    #print(news_p)

    #not needed but retrieved for future development
    teaser=articles.find("div", class_="rollover_description_inner").text

    #Adding to dict
    marsDict["newsTitle"]=newsTitle
    marsDict["news_p"]=news_p


    print("TITLE AND DESCRIPTION OF LATEST NEWS ARTICLE RETRIEVED FROM NASA.")
    print("CONTINUING SCRAPING ACTIVITIES..........")
    #print("..................................")
    print("......................")
    print("...........")
    print(".......")
    print("...")
    ###############################################################################
    ###############  Scraping ... JPL Image Scraping  #############################
    #########################for featured image ###################################

    url_JPL='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    response = requests.get(url_JPL)
    soup = bs(response.text, 'lxml')

    img_jpl = soup.find("img", class_="thumb")["src"]

    #FEATURED IMAGE LINK
    featured_img_url="https://www.jpl.nasa.gov/"+img_jpl
    #print(featured_img_url)

    #!!!!!!!!!!!!!!!!!!!additional depencies to save image to jpeg and print jpeg in workbook. !!!!!!!!!!!

    #Using the 'requests' library to convert url to jpeg

    img_data = requests.get(featured_img_url).content
    with open('Mars_Featured.jpg', 'wb') as handler:
        handler.write(img_data)

    #from IPython.display import Image
    #Image(url='Mars_Featured.jpg')
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


    #img_jpl = soup.find("img", class_="thumb")["src"]
    #featured_img_url="https://www.jpl.nasa.gov/"+img_jpl

    #ADDING TO DICTIONARY
    marsDict["featured_image_url"]= featured_img_url

    print("FEATURED IMAGE OF MARS SCRAPED FROM FROM JPL.")
    print("CONTINUING SCRAPING ACTIVITIES..........")
    #print("..................................")
    #print("......................")
    print("...........")
    print(".......")
    print("...")

    ################################################################################
    ##################  Scraping ... Twitter Weather  ##############################
    ################################################################################


    #Making Scraping Request 
    url_Tweet='https://twitter.com/marswxreport?lang=en'
    response = requests.get(url_Tweet)
    soup = bs(response.text, 'lxml')
    wTweet_jpl = soup.find("div", class_="js-tweet-text-container")

    #Storing Weather
    mars_Weather=wTweet_jpl.find('p').text

    #STORING IN DATABASE
    marsDict["mars_Weather"]= mars_Weather

    print("CURRENT MARS WEATHER ACQUIRED---")
    print("CONTINUING SCRAPING ACTIVITIES..........")
    #print("..................................")
    #print("......................")
    #print("...........")
    print(".......")
    print("...")

    ################################################################################
    #######################  Scraping ... Space Facts ##############################
    ###############Using Pandas to read in table directly###########################
    ################################################################################

    url = 'https://space-facts.com/mars/'

    #!!!!!!!!!!!!!!!!!!
    marsTable = pd.read_html(url)
    df=marsTable[0]
    df.columns=['Mars Feature', 'Data']
    df.set_index('Mars Feature', inplace=True)
    df.to_html('mars_DataTable.html')
    mars_DataTable=df.to_html()
    mars_DataTable= mars_DataTable.replace('\n', '') #Cleaning

    marsDict["mars_dataTable_html"]= mars_DataTable

    print("PHYSICAL FACTS AQUIRED ABOUT MARS---")
    print("ACCESSING ONLINE REPOSITORIES..........")
    #print("..................................")
    #print("......................")
    #print("...........")
    #print(".......")
    print("...")


    ################################################################################
    ###############  Scraping ... for Hemishphere Images  ##########################
    ####################From Astrogeology.usgs.gov##################################
    ################################################################################

    url_ASC='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    response = requests.get(url_ASC)
    soup = bs(response.text, 'lxml')
    hemisphere_urls=[]
    hemis = soup.find_all("div", class_="description")

    ############## Setting up splinter
    executable_path = {'executable_path':'./chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(url_ASC)

    ##############################################################
    ############### Cerberus Hemisphere ##########################
    ##############################################################


    ##### through pages ######
    time.sleep(5)
    browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')

    # BeautifulSoup object (parse with html.parser)
    html = browser.html
    soup = bs(html, 'html.parser')

    # Store link
    Cerberus_Hemisphere_link = soup.find('div', 'downloads').a['href']

    # Create dict
    Cerberus_Hemisphere = {
        "title": "Cerberus Hemisphere Enhanced",
        "img_url": Cerberus_Hemisphere_link
    }

    # Append dict
    hemisphere_urls.append(Cerberus_Hemisphere)


    ##############################################################
    ############### Schiaparelli Hemisphere ######################
    ##############################################################


    # Setting up splinter
    executable_path = {'executable_path':'./chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(url_ASC)

    # through pages
    time.sleep(5)
    browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')


    # BeautifulSoup object (parse with html.parser)
    html = browser.html
    soup = bs(html, 'html.parser')

    # Store link
    Schiaparelli_Hemisphere_link = soup.find('div', 'downloads').a['href']

    # Create dict
    Schiaparelli_Hemisphere = {
        "title": "Schiaparelli Hemisphere",
        "img_url": Schiaparelli_Hemisphere_link
    }

    # Append dict
    hemisphere_urls.append(Schiaparelli_Hemisphere)


    ##############################################################
    ############### Syrtis Major Hemisphere ######################
    ##############################################################


    # Setting up splinter
    executable_path = {'executable_path':'./chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(url_ASC)

    # through pages
    time.sleep(5)
    browser.click_link_by_partial_text('Syrtis Major Hemisphere Enhanced')


    # BeautifulSoup object (parse with html.parser)
    html = browser.html
    soup = bs(html, 'html.parser')

    # Store link
    Syrtis_Major_Hemisphere_link = soup.find('div', 'downloads').a['href']

    # Create dict
    Syrtis_Major_Hemisphere = {
        "title": "Syrtis Major Hemisphere",
        "img_url": Syrtis_Major_Hemisphere_link
    }

    # Append dict
    hemisphere_urls.append(Syrtis_Major_Hemisphere)


    ##############################################################
    ############### Valles Marineris Hemisphere ##################
    ##############################################################


    # Setting up splinter
    executable_path = {'executable_path':'./chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(url_ASC)

    # through pages
    time.sleep(5)
    browser.click_link_by_partial_text('Valles Marineris Hemisphere Enhanced')


    # BeautifulSoup object (parse with html.parser)
    html = browser.html
    soup = bs(html, 'html.parser')

    # Store link
    valles_link = soup.find('div', 'downloads').a['href']

    # Create dict
    valles_marineris = {
        "title": "Valles Marineris Hemisphere",
        "img_url": valles_link
    }

    # Append dict
    hemisphere_urls.append(valles_marineris)

    #ADD DICTIONARY TO MONGO
    marsDict["hemispher_urls"]= hemisphere_urls


    print("IMAGES OF MARS ACQUIRED --------")
    print("SCRAPING COMPLETE..........")
    #print("..................................")
    #print("......................")
    #print("...........")
    #print(".......")
    #print("...")

    return marsDict

data = scrape_f()
print(data)