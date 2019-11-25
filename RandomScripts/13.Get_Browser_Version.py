from selenium import webdriver

#                      Explaination
# here we are going to , get chrome browser version  


#chromepath = r"c:/chrome/chromedriver.exe";

browser = webdriver.Chrome()
browser.get("https://google.com")

print ("Version: "+browser.capabilities['version'])

browser.close()
