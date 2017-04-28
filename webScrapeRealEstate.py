#!/usr/local/opt/python3/bin/python3
import requests
import pandas
from bs4 import BeautifulSoup

url1="http://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/"
# url2="http://www.century21.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/"
r=requests.get(url1)
c=r.content
soup=BeautifulSoup(c,"html.parser")

# mls=soup.find_all("div",{"class":"propertyMLS"})
# for x in mls:
#    #print(x.find_all("h2")[0].text)
#    print(x.text)
# price=soup.find_all("h4",{"class":"propPrice"})
# for y in price:
#     print(y.text)


# all=soup.find_all("div",{"class":"propertyRow"})
# price=all[0].find_all("h4",{"class":"propPrice"})
# print(price[0].text.replace(" ","").replace("\n",""))

page_nr = len(soup.find_all("a",{"class":"Page"}))
page_nr = page_nr*10
# page_nr = soup.find_all("a",{"class":"Page"})[-1].text
# page_nr = int(page_nr)
# page_nr = page_nr*10

l=[]
base_url="http://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="
for page in range(0,page_nr,10):
    url=base_url+str(page)+".html"
    r=requests.get(url)
    c=r.content
    soup=BeautifulSoup(c,"html.parser")
    # print(soup.prettify())
    all=soup.find_all("div",{"class":"propertyRow"})
    # print(all)
    for item in all:
        d={}
        d["Price"]=item.find_all("h4",{"class":"propPrice"})[0].text.replace(" ","").replace("\n","")
        d["Address"]=item.find_all("span",{"class","propAddressCollapse"})[0].text
        try:
            d["Locality"]=item.find_all("span",{"class","propAddressCollapse"})[1].text
        except:
            d["Locality"]=None
        try:
            # Beds
            # print(item.find_all("span",{"class","infoBed"})[0].text)
            d["Beds"]=item.find_all("span",{"class","infoBed"})[0].find("b").text
        except:
            d["Beds"]=None
        try:
            # Baths
            # print(item.find_all("span",{"class","infoValueFullBath"})[0].text)
            d["FullBaths"]=item.find_all("span",{"class","infoValueFullBath"})[0].find("b").text
        except:
            d["FullBaths"]=None
        try:
            # Half Bath?
            # print(item.find_all("span",{"class","infoValueHalfBath"})[0].text)
            d["HalfBaths"]=item.find_all("span",{"class","infoValueHalfBath"})[0].find("b").text
        except:
            d["HalfBaths"]=None
        try:
            # Square Feet
            # print(item.find_all("span",{"class","infoSqFt"})[0].text)
            d["SquareFootage"]=item.find_all("span",{"class","infoSqFt"})[0].find("b").text
        except:
            d["SquareFootage"]=None

        cg=item.find_all("div",{"class","columnGroup"})
        for colgrp in cg:
            fg=colgrp.find_all("span",{"class","featureGroup"})
            fn=colgrp.find_all("span",{"class","featureName"})
            for feature_group, feature_name in zip(fg,fn):
                # print(feature_group.text, feature_name.text)
                if "Lot Size" in feature_group.text:
                    d["LotSize"]=feature_name.text

        l.append(d)
        
df=pandas.DataFrame(l)
df=df[['Price','Address','Locality','Beds','FullBaths','HalfBaths','SquareFootage']]
print(df)
df.to_csv("Output.csv")
