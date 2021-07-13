import requests as rq
from requests.auth import HTTPBasicAuth
import  sys
sys.path.append('/Users/ajang/Desktop/Repositories/DataScience')
import Dir_Srabbing.disableRequest as sb

loginUrl = 'https://www.trademap.org/Index.aspx'
username = 'v_diwan@ssseurope.onmicrosoft.com'
passwrod = 'ywrUt5ZWj6#5iX!'


results = rq.get(loginUrl,auth=HTTPBasicAuth(username,passwrod),verify=False)

statusCode = results.status
data = results.text

print(data)
print()