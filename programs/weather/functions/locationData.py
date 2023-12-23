import requests

def get_location_ip():
    try:
        # Find location via IP address. 
        response = requests.get('https://ipinfo.io')
        data = response.json()
   
        location_data = {
        'ip_address': '',
        'city': '',
        'state': '',
        'gps_loc': ''
        }

        location_data['ip_address'] = data['ip']
        location_data['city'] = data['city']
        location_data['state'] = data['region']
        location_data['gps_loc'] = data['loc']

        for key, value in location_data.items():
            if isinstance(value, str):
                location_data[key] = value.lower()
                
        print(location_data)

        return location_data

    except Exception as err:
        print(f'There has been a error: ----> {err}')

