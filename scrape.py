# http://apidev.accuweather.com/climo/v1/normals/[year]/12/[date]25/48169?apikey=PSUHackathon112016

import requests
import csv
from bs4 import BeautifulSoup
import json


def logDataCSV(separated):
    myfile = open("log.txt", 'a')
    for element in separated:
        #print(element+" TEST")
        myfile.write(element+";")
    myfile.write("\n")
   
    
    
def separateResults(html):
    """Displays text of separated div tags in form of a
    dictionary ("incident#","occurred","reported","nature","offenses","location","disposition")"""
    #ans=["incident#","occurred","reported","nature","offenses","location","disposition"] 
    
    elements=html.text.splitlines() #split information by each new line into list
    ans=[]#start empty list
    
    for element in elements:
        if(len(element)>1):
            if(element.find("charged with")):
                ans.append(element[element.find(":")+1:])
            else:
                ans.append(element[element.find(":")+3:])#substring so only information is shown, then append
        
    return ans



month=1
monthspan=12
year=1960
day=19
dataAvailable=True
locationKey="6789_PC"#State College, PA
key="PSUHackathon112016"
while month<=monthspan: # are there still pages to scrape
    print("Printing data for "+str(month)+"/"+str(day)+"/"+str(year))
    url= "http://apidev.accuweather.com/climo/v1/normals/"+str(year)+"/"+str(month)+"/"+str(day)+"/"+locationKey+"?apikey="+key
    raw= requests.get(url)# request the raw html text from psu incident log
    month+=1
    soup = BeautifulSoup(raw.text,"html.parser")# lets take this raw text and put it into a filter that does nothing yet.
    c=json.loads(str(soup))
    print("Temperature: ", c["Normals"]["Temperatures"]["Average"]["Imperial"]["Value"])
    print("Precipitation: ", c["Normals"]["Precipitation"]["Imperial"]["Value"])
    # print(c.Precipitation)
    # print(c["Precipitation"])
    # print(soup)
    # crimeSet=soup.find_all("div",{"class": "views-row"})# gets each chunk of crime log (holds all data for each incident)
    

        
