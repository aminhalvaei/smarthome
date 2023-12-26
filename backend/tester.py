from weather import configs
import requests

latitude, longitude = 32.640801 ,51.657988
unit = configs.UNITS_OF_MEASUREMENT
api_key = configs.WEATHER_API_KEYS[0]
constant_url = configs.CONSTANT_URL

api_url = f"{constant_url}?lat={latitude}&lon={longitude}&appid={api_key}&units={unit}"

response = requests.get(api_url)

print(response.json())