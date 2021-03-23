from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import tkinter as tk
from tkinter import messagebox
import time, requests, random
from bs4 import BeautifulSoup
import sys
import re
import json
import logging

#comment/uncomment the line underneath to have debug log displayed/not displayed
#logging.basicConfig(level=logging.DEBUG)

i = 0
lookuplist = []
stuffishere = []
root= tk.Tk()

data = {}
FinalDictionnary = {}

#please enter your credential email and password
user = ""
Passwd = ""

#open the List of url to go through it and look them up
with open('ListURL.txt') as f:
    lines = f.read().splitlines()
    lookuplist = lines

listlength = len(lookuplist)

# you will be told the length of your list at the very beginning
print(listlength)

#important verify that the geckodriver is present in the folder
# and check for the lastest version if this one doesn't work
browser = webdriver.Firefox(executable_path="./geckodriver")

yolo = lookuplist[i]    

#first page it will look for is obviously the login
browser.get('https://www.linkedin.com/uas/login')
#it will enter your credential and log as you
ID = browser.find_element_by_id('username')
ID.send_keys(user)

ID = browser.find_element_by_id('password')
ID.send_keys(Passwd)

ID.submit()

time.sleep(10)

browser.execute_script("window.open('');")

#here is the big while loop that will go through all URL in the list 
#load the page and take the information needed
# if modification is necessary i hope you know HTML better than I
# to select the information you have to manually go on the desired page and look
# at the source code and selecte the specific place where the information is stored
while i < listlength:
    file_object = open('TempResult.txt','a')
    info = []
    info2 = []
    yolo = lookuplist[i] 
    print(i)
    file_object.write("\n")
    file_object.write(str(i)+"\n")
    print(yolo)
    file_object.write(yolo+"\n")

    #browser.execute_script("window.open('');")

    browser.switch_to.window(browser.window_handles[1])
    browser.get(yolo)
    #browser.close()
    
    time.sleep(5)

    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(5)

    
    info.append(yolo)

    #those try and except are here to avoid errors due to differences
    #in the source code of different pages
    try:
        PageSRC = browser.page_source
        FilteredSRC = BeautifulSoup(PageSRC, "lxml")
    except:
        PageSRC = browser.page_source
        FilteredSRC = BeautifulSoup(PageSRC, "lxml")

    try:
        nameTAG = FilteredSRC.find('div', {'class': 'flex-1 mr5'})

        nameANDloc = nameTAG.find_all('ul')
        try:
            name = nameANDloc[0].find('li').get_text().strip()
            info.append(name)
        except:
            name = "ERROR"
            info.append(name)
        try:
            location = nameANDloc[1].find('li').get_text().strip()
            info.append(location)
        except:
            location = "ERROR"
            info.append(location)
        try:
            ProfileTitle = nameTAG.find('h2').get_text().strip()
            info.append(ProfileTitle)
        except:
            ProfileTitle = "ERROR"
            info.append(ProfileTitle)
        try:    
            connection = nameANDloc[1].find_all('li')
            connection = connection[1].get_text().strip()
            info.append(connection)
        except:
            connection = "ERROR"
            info.append(connection)
    except:
        print("ERROR nametag")
    

       
    try:
        expSection = FilteredSRC.find('section', {'id': 'experience-section'})
        expSection = expSection.find('ul')
        li_tags = expSection.find('div')
        aTags = li_tags.find('a')

        jobTitles = aTags.find('h3').get_text().strip()
        info.append(jobTitles)
    except:
        
        info.append("ERROR")

      
    try:
        companyname = aTags.find_all('p')[1].get_text().strip()
        info.append(companyname)
    except:
        #print('went the other way')
        companyname = aTags.find('h3').find_all('span')[1].get_text().strip()
        
        logging.debug('company name: %s \n', companyname)
        
        info.append("ERROR")


    try:
        dates = aTags.find_all('h4')[0].find_all('span')[1].get_text().strip()
        info.append(dates)
    except:
        info.append("ERROR")

    try:
        duration = aTags.find_all('h4')[1].find_all('span')[1].get_text().strip()
        info.append(duration)
    except:
        try:
            duration = aTags.find_all('h4')[0].find_all('span')[1].get_text().strip()
            info.append(duration)
        except:
            try:
                #print('went the other way')
                duration = aTags.find_all('h4')
                #print(duration)
                durationSTR = str(duration)
                logging.debug("\n")
                logging.debug(durationSTR)
                logging.debug("\n")
                
                newSTR = durationSTR.split("\n",2)[2]
       
                logging.debug('newstring: %s \n', newSTR)
                
                start = newSTR.find("<span>") + len("<span>")
                end = newSTR.find("</span>")
                substring = newSTR[start:end]
                
                logging.debug('duration: %s \n',substring)

                duration = substring
                info.append(duration)
            except:
                duration = "ERROR"
                info.append(duration)


    #print(info)
    
    #here is whereeverything is store
    name = info[1]
    name2 = info[1]
    name2 = name2.replace(' ', '.')
    email = name2 + '@EnterHostnameOfTheCompany.com'
    
    info2.append(email)
    info2.append(yolo)
    info2.append(name)
    info2.append(info[3])
    info2.append(duration)
   
    file_object.write(email+"\n")
    file_object.write(name+"\n")
    file_object.write(info[3]+"\n")
    file_object.write(duration+"\n")

    #print(info2)

    FinalDictionnary[i] = info2
    data[i] = info
    
    file_object.close()
    
    #with open('ResultLinkedInScrapping.json', 'w') as fp:
    #    json.dump(FinalDictionnary, fp,  indent=4)





    #print(data[i])
    i = i + 1    




#print(data)
#print(FinalDictionnary)


