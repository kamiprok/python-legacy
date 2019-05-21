import requests

with requests.Session() as s:
        s.get('https://netflix.com/')
