#!/usr/bin/env python
# coding: utf-8

# In[35]:


# Importing libraries
import urllib.request, urllib.error, urllib.parse
import json
# Sample data test: http://py4e-data.dr-chuck.net/comments_42.json
# Actual data test: http://py4e-data.dr-chuck.net/comments_1786548.json

location = input('Enter location: ')
print('Retrieving ', location)
url = urllib.request.urlopen(location).read()
decodedextract = url.decode()
cleanextract = json.loads(decodedextract)
# formatextract = json.dumps(cleanextract, indent = 2)
# print(formatextract)
print('Retrieved', len(decodedextract),'characters')
lst = []
sum = 0
# Looping through the json
for num in cleanextract["comments"]:
    lst.append(int(num["count"]))
    sum = sum + num["count"]
print('Count:', len(lst))
print('Sum:', sum)


# In[ ]:




