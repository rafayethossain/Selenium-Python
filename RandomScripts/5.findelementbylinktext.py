from selenium import webdriver


#                                     Explaination
# in this tutorial we are going to select link with its text 



browser = webdriver.Chrome()
browser.get('https://google.co.uk')

try:
    browser.find_element_by_link_text('About')
    print('Test Pass : Link Text Found ')
except Exception as e:
    print ('Exception Found ', format(e))

browser.close()

