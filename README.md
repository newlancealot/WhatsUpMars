# WhatsUpMars
Bootcamp HW assigment

Part 1
This assigment required data scraping from the following sources:
<l>NASA Mars News Site (https://mars.nasa.gov/news/)
    Latest News Title and Paragraph Text
    Variables Created:
         newsTitle
         NewsParagraph
         
<2> JPL Mars (https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars)
    Used to find and captured the lastest image of mars using 'Splinter' and save it as a .jpg.
    Variables Created:
        featured_image_url

<3>Mars Weather Twitter Pages (https://twitter.com/marswxreport?lang=en)
    Used to scrape the latest Mars weather Tweet and save it
    Variables Created:
        mars_weather

<4> Mars Facts Webpage (https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars)
    This page will provide facts on the Red Planet includeing Diameter, Mass, etc. The data will be converted to a HTML table string using Pandas

<5> USGS Astrogeology site (https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars)
    High resolution images of each of Mar's hemispheres will be obtained. 

Part 2
MongoDB and Flask were used to create a HTML page that displays all of the collected information. 
    Required code
        Scrape_mars.py (which complies the scraping done in the Part 1)
            Major Functions
                scrape - executes all the scraping code
        Routes to create:
            /scrape - store the return value in a mongo as a python dictionary
            /root - query your Mongo DB and pass the mars data into an HTML Template to display the data
        