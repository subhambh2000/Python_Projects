import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error # noqa
# from bs4 import BeautifulSoup
import ssl
# # Ignore SSL certifcate error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
# data = '''<stuff>
#     <users>
#         <user x="2">
#             <id>001</id>
#             <name>Chuck</name>
#         </user>
#         <user x="7">
#             <id>007</id>
#             <name>Brent</name>
#         </user>
#     </users>
# </stuff>'''
url = input('Enter URL: ')
xml = urllib.request.urlopen(url,context=ctx)
data = xml.read()
stuff = ET.fromstring(data)
lst = stuff.findall('.//comment')
# print('User count:',len(lst))
s = 0
for i in lst:
    s += int(i.find('count').text)
    # print('count:',i.find('count').text)
    # print('Id:',i.find('id').text)
    # print('Attribute',i.get("x"))
print('sum:',s)
