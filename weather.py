# MyApiKey :  920a988965d6499398766ffb242a27e3    use Your Own API KEY

api_key = '920a988965d6499398766ffb242a27e3'

import requests

def get_by_location():
    # Get The Location of the user using the 'freegeoip' service which provides the user's location through IP.
    freegeoip_url = "http://freegeoip.net/json"
    location_raw = requests.get(freegeoip_url)
    location_json = location_raw.json()
    # get the user's longitude and latitude
    longitude = location_json['longitude']
    latitude = location_json['latitude']
    # print(longitude,latitude)  Use this for testing purposes

    # Get the weather a user's location based on the detected longitude and latitude
    raw_data = requests.get("https://api.weatherbit.io/v2.0/current?&lat={}&lon={}&key={}".format(latitude,longitude,api_key))
    weather_json = raw_data.json()
    return weather_json
    # print(weather_json) Use this for testing purposes


def get_by_city(city):
    raw_data = requests.get("https://api.weatherbit.io/v2.0/current?city={}&key={}".format(city,api_key))
    weather_json = raw_data.json()
    return weather_json
    # print(weather_json)  user for testing purposes

if __name__ == '__main__':
    get_by_city(None)
    get_by_location()

# Sample JSON Output from the weatherbit api

# {'count': 1, 'data': [{'timezone': 'Asia/Kolkata', 'datetime': '2018-02-02:17', 'uv': 0, 'precip': 0, 'country_code': 'IN', 'lon': 87.33, 'app_temp': 20.8, 'elev_angle': -56, 'ob_time': '2018-02-02 15:30', 'pod': 'n', 'snow': 0, 'sunrise': '00:44', 'clouds': 0, 'weather': {'code': '800', 'icon': 'c01n', 'description': 'Clear sky'},
#                        'state_code': '28', 'wind_cdir': 'SW', 'wind_spd': 1.1, 'dewpt': 10.5, 'slp': 1015, 'ts': 1517590800, 'temp': 21.3, 'vis': 10, 'wind_cdir_full': 'southwest', 'wind_dir': 225, 'h_angle': -90, 'rh': 50.1, 'pres': 1010, 'station': 'VECC', 'dhi': 0, 'lat': 22.33, 'sunset': '11:55', 'city_name': 'Kharagpur'}]}
