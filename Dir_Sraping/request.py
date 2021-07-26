import requests as rq
from requests.auth import HTTPBasicAuth
import  sys
sys.path.append('/Users/ajang/Desktop/Repositories/DataScience')
import Dir_Sraping.disableRequest as sb

loginUrl = 'https://www.trademap.org/Index.aspx'
username = 'v_diwan@ssseurope.onmicrosoft.com'
passwrod = 'ywrUt5ZWj6#5iX!'
token = "XYCKsqjUT2l7_-UKDMrL4eOhoN2hTHHP1_gS500Zuf0"

# results = rq.get(loginUrl,auth=HTTPBasicAuth(username,passwrod),verify=False)
results = rq.get(loginUrl,headers={'Authorization': token})

statusCode = results.status
data = results.text

print(data)
print()