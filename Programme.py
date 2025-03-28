#import xmltodict
#import json
import requests

_BASE = "https://live.pim.wilkhahn.sepia.de/awx/api/objects/1/2/contexts"
_SID = "export"
_PATH = "/1/2"
_CLASS = "wilkhahn:CATEGORY_PROGRAM"
#api_url = "https://live.pim.wilkhahn.sepia.de/awx/api/objects/wilkhahn/search?sid=export&path_filter=/1/2"
#api_url = f"{_BASE}?sid={_SID}&path_filter={_PATH}&class={_CLASS}"
#https://live.pim.wilkhahn.sepia.de/awx/api/objects/wilkhahn/search?sid=export&recursive=0&protopath=demo://{r=0,b=0,l=de_DE}/1/2

api_url = f"{_BASE}?sid={_SID}"

response = requests.get(api_url)
#response.json()

print(api_url)
print (response)
print (response.headers)
