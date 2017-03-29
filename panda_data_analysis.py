# #!/usr/local/bin/python3
# See below for more examples 

import pandas
from geopy.geocoders import Nominatim
df6 = pandas.read_csv("http://pythonhow.com/supermarkets.csv")
df6 = df6.set_index("ID")
df6["Continent"]=["America","America","America","America","America","America"]
df6["Continent"] = df6.shape[0]*["America"]
df6["Continent"] = "North " + df6["Continent"]
df6_t=df6.T
df6_t[7]=["3157 Dallas Ct", "Santa Clara", "CA 95051", "USA", "John", "1", "North America"]
df6=df6_t.T
nom = Nominatim(scheme='http')
df6["Address"]=df6["Address"]+" "+df6["City"]+" "+df6["State"]+" "+df6["Country"]
df6=df6.drop("Continent",1)
df6["Coordinates"]=df6["Address"].apply(nom.geocode)
print(df6.Coordinates[7])
df6["Latitude"]=df6["Coordinates"].apply(lambda x: x.latitude if x != None else None)
df6["Longitude"]=df6["Coordinates"].apply(lambda x: x.longitude if x != None else None)
print(df6.loc[7,"Latitude":"Longitude"])
#print(df6)

# import pandas
# from geopy.geocoders import Nominatim
# # import os
# # print(os.listdir())
# 
# # df1 = pandas.DataFrame([[2,4,6],[10,20,30]], columns=["Price","Age","Farts"], index=["1st","2nd"])
# # 
# # print(df1)
# # 
# # df2 = pandas.DataFrame([{"First":"John","Last":"Goodman"},{"First":"Linda","Last":"Goodman"}])
# # print(df2)
# # 
# # print(df1.mean())
# # print(df1.mean().mean())
# # print(df1.Price.mean())
# # print(df1.Price.max())
# 
# # df1 = pandas.read_csv("supermarkets.csv")
# # # To turn the header off: pandas.read_csv("supermarkets.csv",header=None)
# # # print(df1)
# # print(df1.set_index("ID"))
# # print(df1.shape)
# 
# # df2 = pandas.read_json("supermarkets.json")
# # print(df2.set_index("ID"))
# # 
# # df3 = pandas.read_excel("supermarkets.xlsx",sheetname=0)
# # print(df3.set_index("ID"))
# 
# # df4 = pandas.read_csv("supermarkets-commas.txt")
# # print(df4.set_index("ID"))
# 
# # df5 = pandas.read_csv("supermarkets-semi-colons.txt", sep=";")
# # print(df5.set_index("ID"))
# ### READ FROM THE INTERNET!!
# df6 = pandas.read_csv("http://pythonhow.com/supermarkets.csv")
# # Can set the index to any of the columns, such as Address or Country...
# # Also remember to save the new data frame into a variable else you will lose it
# df6 = df6.set_index("ID")
# # print(df6)
# # # Label based versus Position Based indexing
# # print(df6.loc["1":"4","Address":"State"])
# # print(df6.loc["2":"3","State"])
# # print(df6.loc[1,"State"])
# # print(df6.iloc[1:3,1:3])
# # print(df6.iloc[1:,1:4])
# # print(df6.ix[1,"Name"])
# # print(df6.ix[3:,"Name"])
# # DROP A COLUMN. COLUMN is 1, ROW is 0
# # print(df6.drop("City",1))
# # # DROP A ROW
# # print(df6.drop(1,0))
# # print(df6.drop(df6.index[0:3],0))
# # print(df6.drop(df6.columns[0:3],1))
# #print(len(df6.index))
# 
# df6["Continent"]=["America","America","America","America","America","America"]
# df6["Continent"] = df6.shape[0]*["America"]
# #print(df6)
# df6["Continent"] = "North " + df6["Continent"]
# #print(df6)
# df6_t=df6.T
# #print(df6_t)
# df6_t[7]=["3157 Dallas Ct", "Santa Clara", "CA 95051", "USA", "John", "1", "North America"]
# #print(df6_t)
# df6=df6_t.T
# # print(df6)
# nom = Nominatim(scheme='http')
# # print(nom.geocode("3157 Dallas Ct, Santa Clara, CA 95051"))
# # print(nom.geocode("2845 Lafayette St, Santa Clara, CA 95050"))
# # ardit=nom.geocode("3995 23rd St, San Francisco, CA 94114", addressdetails=True)
# # print(str(ardit.latitude) + " " + str(ardit.longitude))
# 
# df6["Address"]=df6["Address"]+" "+df6["City"]+" "+df6["State"]+" "+df6["Country"]
# df6["Coordinates"]=df6["Address"].apply(nom.geocode)
# print(df6["Coordinates"])


















