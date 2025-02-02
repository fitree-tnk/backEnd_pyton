import requests

API_key = "446c26a524930863af2240db722fc497"
city = "bangkok"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"

result = requests.get(url).json()

print(result)
city_name = result['name']
country = result['sys']["country"]
weather = result['weather'][0]['main']
description = result['weather'][0]['description']
temp = result['main']['temp'] - 237.15

print(f"เมือง {city_name} ประเทศ {country}")
print(f"สภาพอากาศ {weather} มีลักษณะ {description}")
print(f"อุณหภูมิ {temp}")