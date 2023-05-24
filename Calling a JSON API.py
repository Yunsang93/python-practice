#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Importing libraries
import urllib.request, urllib.error, urllib.parse
import json
import ssl

api_key = False
if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: 
        break
    parms = dict()
    parms['address'] = address
    
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    js = json.loads(data)
#     print(json.dumps(js, indent = 2))
    print("Place Id", js["results"][0]["place_id"])
    break


# In[ ]:




