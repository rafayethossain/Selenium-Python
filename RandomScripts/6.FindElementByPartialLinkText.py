
from selenium import webdriver


#                                     Explaination
# in this tutorial we are going to select link that contains specific text  



browser = webdriver.Chrome()
browser.get('https://www.wikipedia.org/')

try:
    browser.find_element_by_partial_link_text('Terms')
    print('Test Pass :Partial Link Text Found ')
except Exception as e:
    print ('Exception Found ', format(e))
    
browser.close()
