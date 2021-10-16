from re import search
import requests
from bs4 import BeautifulSoup
import json

page = requests.get("https://scoop.eduncle.com/indian-national-government-organizations-agency")
soup = BeautifulSoup(page.text,"html.parser")

def scrap_data():
    div = soup.find("div",class_="table-responsive")

    body = div.find("tbody")

    tr = body.find_all("tr")
    
    organization = []
    estab_year = []
    abbreviation = []
    logo=[]

    for i in tr:
 
        name = i.find("td",width="148").get_text()
        organization.append(name)
       
        ab = i.find("td",width=123).get_text()[1:-1]
        abbreviation.append(ab)

        year = i.find("td",width="122").get_text()
        estab_year.append(year)

        image = i.find("td",width="116").get_text()
        logo.append(image)
        print(image,logo)
    
    oranisation_data = {}
    list = []
    index = 1
    serial_no = 1

    while index<len(estab_year):

        oranisation_data["Searial_no."] = serial_no
        oranisation_data["Oranisation_name"] = organization[index]
        oranisation_data["Abbreviation"] = abbreviation[index]
        oranisation_data["Foundation_Date"] = estab_year[index]
        oranisation_data["Logo"]=logo[index]
        list.append(oranisation_data.copy())

        index += 1
        serial_no += 1
        
    
        with open("Oragnisation_detail.json","w+") as info:
            json.dump(list,info,indent = 4)

scrap_data()