import socket


# internal IP
# in_addr = socket.gethostbyname(socket.gethostname())
# print(in_addr)


# internal IP with connecting
# in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# in_addr.connect(("www.google.co.kr", 443))
# print(in_addr.getsockname()[0])


# external IP
import requests
import re
# req = requests.get("http://ipconfig.kr")
# out_addr = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]
# print(out_addr)


in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
in_addr.connect(("www.google.co.kr", 443))
print(" internal IP: ", in_addr.getsockname()[0])

req = requests.get("http://ipconfig.kr")
out_addr = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]
#re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]
print(req.text)
print(" external IP: ", out_addr)