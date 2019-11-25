from selenium import webdriver
import requests 
import validators
 
 
 

text_file = open("dgdaUrl.txt", "r")
links = text_file.readlines()

print ("\nNo of links:"+str(len(links)))

for url in links:
    r = requests.get(url)
    #print(url+ ": "+ str(r.status_code))
    if r.status_code ==200:
        print("\n\n\n Page Url: "+url+ "\n status: "+str(r.status_code)+ " - OK")
    elif r.status_code == 401:
        print( "\n\n\n Page url: "+url+"\n status: "+str(r.status_code)+ " -UnAthurized")
        #print(url+" -is broken, \n status is: "+str(r.status_code))
    elif r.status_code == 403:
        print( "\n\n\n Page url: "+url+"\n status: "+str(r.status_code)+ " -Forbidden")
    elif r.status_code == 404:
        print( "\n\n\n Page url: "+url+"\n status: "+str(r.status_code)+ " -page not found")
    elif r.status_code == 500:
        print( "\n\n\n Page url: "+url+"\n status: "+str(r.status_code)+ " -Internal server error")
    elif r.status_code == 403:
        print( "\n\n\n Page url: "+url+"\n status: "+str(r.status_code)+ " -Service Unable")
    else:
        print( "\n\n\n Page url: "+url+"\n status: "+str(r.status_code)+ " -for more info google it")

 

print("\n \t\tDone !")
