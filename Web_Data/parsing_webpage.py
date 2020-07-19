# import socket
import urllib.request, urllib.parse, urllib.error # noqa
from bs4 import BeautifulSoup
import ssl
# # Ignore SSL certifcate error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
# # Using Socket opening and reading a web page
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org',80))
# cmd = 'GET  HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)
# while True:
#     data = mysock.recv(512)
#     if len(data) < 1:
#         break
#     print(line.decode().strip())
# mysock.close()
# #  Using urllib for a opening and reading a web page
# fh = urllib.request.urlopen('http://data.pr4e.org/intro-short.txt')
# fh = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
# for line in fh:
#     print(line.decode().strip())
# # Using urllib and beautiful soup parsing a web page from a user enterred url
url = input('Enter URL: ')
count = int(input('Enter count: '))
po = int(input('Enter position: '))
while count > 0:
    html = urllib.request.urlopen(url,context=ctx).read()
    soup = BeautifulSoup(html,'html.parser')
    # Retrieve all of the anchor type
    tags = soup('a')
    # suM = 0
    tag = tags[po-1]
    # print('TAG:', tag)
    name = tag.contents[0]
    url = tag.get('href')
    # suM += int(tag.contents[0])
    # print('Attrs:', tag.attrs)
    # print(suM)
    count -= 1
print(name) # noqa
