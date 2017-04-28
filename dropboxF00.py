#!/usr/local/opt/python3/bin/python3

import dropbox, json
# Get your app key and secret from the Dropbox developer website
# app_key = 'w6qfhjki6pwaqii'
# app_secret = 'x1bhinl5y5aax5n'
access_token="gotvwZXSdUsAAAAAAAAI5j_IYSyRbSzNcWyZvVy_w7FjYCl4C4XIlvlf5UGzpGPD"


# flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)
# # Have the user sign in and authorize this token
# authorize_url = flow.start()
# print('1. Go to: ' + authorize_url)
# print('2. Click "Allow" (you might have to log in first)')
# print('3. Copy the authorization code.')
# code = input("Enter the authorization code here: ").strip()
# # This will fail if the user enters an invalid authorization code
# access_token, user_id = flow.finish(code)
# client = dropbox.client.DropboxClient(access_token)
# print('linked account: ', client.account_info())
# print(access_token)

client = dropbox.client.DropboxClient(access_token)
### UPLOAD TO DROPBOX
# f = open('volcanos.html', 'rb')
# response = client.put_file('/volcanos.html', f)
# print("uploaded:", response)

### LIST DROPBOX
folder_metadata = client.metadata('/')
a = len(folder_metadata["contents"])
for x in range(a):
    print(folder_metadata["contents"][x]["path"])

### DOWNLOAD FROM DROPBOX
# f, metadata = client.get_file_and_metadata('/volcanos.html')
# out = open('volcanos2.html', 'wb')
# out.write(f.read())
# out.close()
# print(metadata)





#print(folder_metadata["contents"][0]["path"])
#print(folder_metadata["contents"]["0"]["path"])



# print("metadata:", folder_metadata)
