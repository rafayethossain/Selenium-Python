# First, we'll use selenium to get the page and grab all the links and images from the page:
from selenium import webdriver
import requests 
import validators
 
 
driver = webdriver.Chrome()
#driver =webdriver.Firefox()

driver.get("http://dgda.qa:81/")
links = driver.find_elements_by_css_selector("a")
images = driver.find_elements_by_css_selector("img")

#totalLink = len(links)
print("Number of links:", len(links))
urls = []
for link in links:
    #print(link.get_attribute("href"))
    #urls.append(link.get_attribute("href"))
    #print(url)
    url = link.get_attribute("href")
    #urlValidation = validators.url(url)
    #if urlValidation:
    urls.append(url)
    #print("Url is: "+url+"\n And Status: "+ str(urlValidation))

    

    #urlValidation = validators.url(url)
    #print(urlValidation)
    #if urlValidation:
        #r = requests.get(url)
        #print(url+ ": "+ str(r.status_code))
       # print(url+ "\n")

        
    #else:
        #print(url+ "\n")
        #r= requests.get(url)
        #print(url+ ": "+ str(r.status_code))
f = open("demofile.txt", "w")
for i in urls:
     f.write(str(i))
     f.write("\n")
f.close()

#print(urls)
#for url in urls:
    #urlValidation = validators.url(url)
    #r = requests.get(url)
    #print(url+ ": "+ str(r.status_code))   
        
         
