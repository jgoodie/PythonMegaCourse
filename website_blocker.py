#!/usr/local/bin/python3
import time
from datetime import datetime as dt
# /etc/hosts
#hosts_path="/etc/hosts"
hosts_path="foo_hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com", "www.instagram.com","instagram.com"]

while True:
    workstart = dt(dt.now().year,dt.now().month,dt.now().day,8)
    worknow = dt.now()
    workend = dt(dt.now().year,dt.now().month,dt.now().day,18)
    if workstart < worknow < workend:
        print("Get back to work!!\n")
        with open(hosts_path, 'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + "    " + website + "\n")        
    else:
        print("Go home!!\n")
        with open(hosts_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()

    time.sleep(5)
