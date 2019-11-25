# First, we'll use selenium to get the page and grab all the links and images from the page:
from selenium import webdriver
import requests 

 
 
driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/")
links = driver.find_elements_by_css_selector("a")
images = driver.find_elements_by_css_selector("img")

#totalLink = len(links)
print("Number of links:", len(links)) 
for link in links:
    #print(link.get_attribute("href"))
    url = link.get_attribute("href")
    r = requests.get(url)
    # print(r)
    #print(r.status_code)
    if r.status_code ==200:
        print("Url: "+url+ "\n-is ok")
    elif r.status_code == 401:
        print( "Page url: "+url+"\n status "+str(r.status_code)+ " UnAthurized")
        #print(url+" -is broken, \n status is: "+str(r.status_code))
    elif r.status_code == 403:
        print( "Page url: "+url+"\n status"+str(r.status_code)+ "Forbidden")
    elif r.status_code == 404:
        print( "Page url: "+url+"\n status"+str(r.status_code)+ "page not found")
    elif r.status_code == 500:
        print( "Page url: "+url+"\n status"+str(r.status_code)+ "Internal server error")
    elif r.status_code == 403:
        print( "Page url: "+url+"\n status"+str(r.status_code)+ "Service Unable")
    else:
        print( "Page url: "+url+"\n status"+str(r.status_code)+ "for more info google it")
