import urllib.request,urllib.parse,urllib.error
import json
import ssl
# import twurl
# # GeoJSON API authentication
# api_key = False
# If you have a Google Places API key, enter it here
api_key = 'AIzaSyBw4cpiJhUCMax7hze7VtXe3ufOYhizRyY'
# https://developers.google.com/maps/documentation/geocoding/intro

# if api_key is False:
#     api_key = 42
#     serviceurl = 'http://py4e-data.dr-chuck.net/json?'
# else:
#     serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# # Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
# # Basic JSON parsing
# js = '''
# [
#     {   "id" : "001",
#         "x" : "2",
#         "name" : "Chuck"
#     } ,
#     {   "id" : "009",
#         "x" : "7",
#         "name" : "Chuck"
#     }
# ]'''
#
url = input('Enter Location: ')
print('Retrieving',url)
ub = urllib.request.urlopen(url)
data = ub.read().decode()
print('Retrieved',len(data),'character')

try:
    js = json.loads(data)
except:
    js = None
sm = 0
# print('User Count:',len(info))
for i in js['comments']:
    # print(i["count"])
    sm += int(i["count"])
print('Sum:',sm)
# # Using GeoJSON API
# serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
# while True:
#     address = input('Enter Location: ')
#     if len(address) < 1:
#         break
#     url = serviceurl+urllib.parse.urlencode({'address':address})+'&key='+api_key
#     print('Retrieving',url)
#     ub = urllib.request.urlopen(url)
#     data = ub.read().decode()
#     print('Retrieved',len(data),'character')
#
#     try:
#         js = json.loads(data)
#     except:
#         js = None
#
#     if not js or 'status' not in js or js['status'] != 'OK':
#         print('---Failure to Retrieve---')
#         print(data)
#         continue
#     lat = js["results"][0]["geometry"]["location"]["lat"]
#     lng = js["results"][0]["geometry"]["location"]["lng"]
#     print('Lat',lat,"Lng",lng)
#     location = js['results'][0]['formatted_address']
#     print(location)

