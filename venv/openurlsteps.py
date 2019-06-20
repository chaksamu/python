import requests

r = requests.get('http://www.py4inf.com/code/romeo.txt')
r.status_code
print(r.text)

