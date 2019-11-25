#Getting all url from a page and export into a text file
from selenium import webdriver
import requests 
import time
 
 
driver = webdriver.Chrome()
#driver =webdriver.Firefox()
driver.set_page_load_timeout(10)
driver.implicitly_wait(10)

driver.get("http://dgda.qa:81/")
links = driver.find_elements_by_css_selector("a")
images = driver.find_elements_by_css_selector("img")
 
print("Number of links found:", len(links))
urls = []
for link in links:
    
    url = link.get_attribute("href")
     
    urls.append(url)
 
f = open("dgdaUrl.txt", "w")
for i in urls:
     f.write(str(i))
     f.write("\n")
f.close()

 
   
        
         
