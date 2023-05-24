import requests
import json

location = 'London' 
apiKey = '9775f5021c16f65d74228265721888a7'
r = requests.get('http://api.weatherstack.com/current?access_key=9775f5021c16f65d74228265721888a7&query=London')

data = r.json() 

print(data)