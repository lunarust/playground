from datetime import datetime, timedelta
import requests
import json

startdate = datetime.today() - timedelta(days=7)
enddate = datetime.today()

print(startdate)
print(enddate)

###################################
# SECTION 1: Call for an authentication token
type = 'application/json'
#Input parameters
url = "https://earthquake.usgs.gov/fdsnws/event/1/query&format=geojson?"
parameters = "starttime=" + startdate.strftime("%Y-%m-%dT%H:%M") + "&latitude=37.57086135710454&longitude=22.80949188170508&maxradiuskm=520"
#.strftime("%m/%d/%Y, %H:%M:%S")
payload = {
  "Login": "",    # Your platform username.
  "Password": ""  # Your platform password.
}

#myResponse = requests.post(url, headers={"Content-Type": type}, json=payload)
myResponse = requests.get(url + parameters, headers={"Content-Type": type})

if(myResponse.ok):

  jData = json.loads(str(myResponse.content, "utf-8"))
  response = jData["features"]
  print(response)

else:
  #If response code is not ok (200), print the resulting HTTP error code with description
  myResponse.raise_for_status()

###################################
# SECTION 2: Call the API endpoint you want to test

#Input parameters
#url = "https://api.thetradedesk.com/v3/adgroup/query/advertiser"
#payload = {
#  "AdvertiserId": "",
#  "PageStartIndex": 0,
##  "PageSize": 1
#}
#######################
