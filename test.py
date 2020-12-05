import requests
import json


url = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url="
target = "https://mutaonet.hatenablog.com/"
params = "&category=performance&strategy=mobile"
headers = {"content-type": "application/json"}
response = requests.get(url+ target + params, headers).json()
#print(response["lighthouseResult"]["audits"]["unminified-css"])
res = response["lighthouseResult"]["audits"]["speed-index"]
print(res)
#for r in res:
    #print("r: " + r)
    #print(res)