# Using XPath Selector code
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

location = input('Enter location: ')
print('Retrieving', location)
rawdata = urllib.request.urlopen(location, context=ctx).read()
tree = ET.fromstring(rawdata)
print('Retrieved', len(rawdata),'characters')
counts = tree.findall('.//count')  # This is the XPath Selector code
print('Count: ', len(counts))
sum = 0
for item in counts:
    sum = sum + int(item.text)
print('Sum: ', sum)

# Looping through parent and children tags
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

location = input('Enter location: ')
print('Retrieving', location)
rawdata = urllib.request.urlopen(location, context=ctx).read()
# data = rawdata.decode()
print('Retrieved', len(rawdata),'characters')
tree = ET.fromstring(rawdata)
comments = tree.findall('comments/comment')
listcount = []
for count in comments:
    listcount.append(count.find('count'))
print('Count: ', len(listcount))
sum = 0
for num in listcount:
    sum = sum + int(num.text)
print('Sum: ', sum)