import time
from datetime import datetime
import siaskynet as skynet


now = datetime.now()
today_is = now.strftime("%m/%d/%Y, %H:%M:%S")
# debug print("uploaded at", today_is)

client = skynet.SkynetClient()
url = client.upload_directory("./dataset")
print("Upload successful, url: " + url)
# put the links into txt folder for me!
f= open("skynet_links.txt","w+")
f.write(url + str(today_is))
f.close()
