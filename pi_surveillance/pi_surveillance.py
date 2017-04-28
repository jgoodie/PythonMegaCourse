#!/usr/local/opt/python3/bin/python3

from pyimagesearch.tempimage import TempImage
import dropbox
import warnings
import datetime
import imutils
import json
import time
import cv2


# App key: w6qfhjki6pwaqii
# App secret: x1bhinl5y5aax5n
# Folder: Apps/pi_surveillance_app
# AuthCode: gotvwZXSdUsAAAAAAAAI3RzsREX7FRMbWMoUnAXNQek
access_token="gotvwZXSdUsAAAAAAAAI5j_IYSyRbSzNcWyZvVy_w7FjYCl4C4XIlvlf5UGzpGPD"

conf = json.load(open("conf.json"))
client = dropbox.client.DropboxClient(access_token)


# if conf["use_dropbox"]:
#     # connect to dropbox and start the session authorization process
#     flow = DropboxOAuth2FlowNoRedirect(conf["dropbox_key"], conf["dropbox_secret"])
#     print "[INFO] Authorize this application: {}".format(flow.start())
#     authCode = raw_input("Enter auth code here: ").strip()
#  
#     # finish the authorization and grab the Dropbox client
#     (accessToken, userID) = flow.finish(authCode)
#     client = DropboxClient(accessToken)
#     print "[SUCCESS] dropbox account linked"


