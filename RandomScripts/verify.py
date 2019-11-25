from selenium import webdriver
import requests 
import validators
 
 
 

text_file = open("url.txt", "r")
links = text_file.readlines()

print ("\nNo of links:"+str(len(links)))

urls = []
for link in links:
    urlValidation = validators.url(link)
    if urlValidation:
        urls.append(url)
print(urls)

print("\n \t\tDone !")
