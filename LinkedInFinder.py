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

i = 0
lookuplist = []
stuffishere = []
root= tk.Tk()

data = {}
FinalDictionnary = {}

user = "MrPotatoTheTastiest@protonmail.com"
Passwd = "FrenchFries8"


with open('ListURL.txt') as f:
    lines = f.read().splitlines()
    lookuplist = lines

listlength = len(lookuplist)
print(listlength)

browser = webdriver.Firefox(executable_path="./geckodriver")

yolo = lookuplist[i]    

browser.get('https://www.linkedin.com/uas/login')

ID = browser.find_element_by_id('username')
ID.send_keys(user)

ID = browser.find_element_by_id('password')
ID.send_keys(Passwd)

ID.submit()

time.sleep(10)

browser.execute_script("window.open('');")

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
        #print('company name: ', companyname)
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
        
       #print('\n', durationSTR, '\n')
                newSTR = durationSTR.split("\n",2)[2]
       
       #print('newstring: ', newSTR)
                start = newSTR.find("<span>") + len("<span>")
                end = newSTR.find("</span>")
                substring = newSTR[start:end]
       #print('duration: ',substring)
                duration = substring
                info.append(duration)
            except:
                duration = "ERROR"
                info.append(duration)


    #print(info)
    
    name = info[1]
    name2 = info[1]
    name2 = name2.replace(' ', '.')
    email = name2 + '@hs2.org.uk'
    
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


