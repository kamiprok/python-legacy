import requests

url = "http://172.30.188.163:8080/jmx-console"
username = 'Administrator'
password = 'password'

r = requests.get(url, auth=(username, password))
print(f'status: {r.status_code}')
