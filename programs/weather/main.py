# coding: utf-8
import requests
import json


params = {
  'access_key': '9775f5021c16f65d74228265721888a7',
  'query': 'New York'
}

apiResult = requests.get('https://api.weatherstack.com/current', params)

apiResponse = apiResult.json()

# The u before the string represents uicode
print(u'Current temperature in %s is %d℃' % (apiResponse['location']['name'], apiResponse['current']['temperature']))
# print('Current temperature in {} is {}℃'.format(api_response['location']['name'], api_response['current']['temperature']))