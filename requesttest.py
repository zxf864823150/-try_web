import requests
url = "http://192.168.1.35:5000/geturl"
data = {"name":"zhaixoafan","age":18}
r = requests.post(url,params=data)
print(r.status_code)
print(r.text)