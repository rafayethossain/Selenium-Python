#Getting all url from a page and export into a text file
from selenium import webdriver
import requests 
import time
 
#declaring webdriver 
#driver = webdriver.Chrome()
driver =webdriver.Firefox()
driver.set_page_load_timeout(10)
driver.implicitly_wait(10)
driver.get("http://mis.totthoapa.gov.bd/TotthoApa")


links = driver.find_elements_by_css_selector("a")
images = driver.find_elements_by_css_selector("img")
 
print("Number of links found:", len(links))

#Collecting url on current page
urls = []
for link in links:
    
    url = link.get_attribute("href")
     
    urls.append(url)

#Collecting image links on current page
    
for imgLink in images:
    url =link.get_attribute("href")
    urls.append(url)

    
#Saving url in text file  
f = open("url.txt", "w")

print( "After image adding link: "+ str(len(urls)))
for i in urls:
     f.write(str(i))
     f.write("\n")
f.close()

 
   
        
         
