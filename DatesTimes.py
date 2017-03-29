#!/usr/local/bin/python3 

import os, datetime, time

now=datetime.datetime.now()
yesterday=datetime.datetime(2017,3,8,11,0,0,0)
delta = now - yesterday
after = now + datetime.timedelta(days=2)
aftersec = now + datetime.timedelta(seconds=10002)
print(now)
print(yesterday)
print(now)
print(delta)
print(delta.days)
print(delta.seconds)
print(after)
print(aftersec)


filename = datetime.datetime.now()
def create_file():
    with open("file" + str(filename.strftime("%Y%m%d")) + ".txt", "w") as filehandle:
        filehandle.write(str(filename))
      
        
create_file()
print(os.listdir())

lst = []
for i in range(5):
    lst.append(datetime.datetime.now())
    time.sleep(2)
    
for x in lst:
    print(x)
    
