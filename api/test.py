import requests

# ข้อมูล JSON ที่คุณได้รับจาก API
weather_data = {
    'coord': {'lon': 100.5167, 'lat': 13.75},
    'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}],
    'base': 'stations',
    'main': {
        'temp': 305.73, 
        'feels_like': 305.72, 
        'temp_min': 304.09, 
        'temp_max': 306.45, 
        'pressure': 1008, 
        'humidity': 37, 
        'sea_level': 1008, 
        'grnd_level': 1008
    },
    'visibility': 10000,
    'wind': {'speed': 2.05, 'deg': 116, 'gust': 2.01},
    'clouds': {'all': 100},
    'dt': 1737441548,
    'sys': {'type': 2, 'id': 2093772, 'country': 'TH', 'sunrise': 1737416742, 'sunset': 1737457938},
    'timezone': 25200,
    'id': 1609350,
    'name': 'Bangkok',
    'cod': 200
}

# ดึงค่าต่าง ๆ
city = weather_data.get("name", "Unknown")
country = weather_data["sys"].get("country", "Unknown")

# แปลงค่าอุณหภูมิเป็นองศาเซลเซียส
temperature = round(weather_data["main"].get("temp", 0) - 273.15, 2)
feels_like = round(weather_data["main"].get("feels_like", 0) - 273.15, 2)
temp_min = round(weather_data["main"].get("temp_min", 0) - 273.15, 2)
temp_max = round(weather_data["main"].get("temp_max", 0) - 273.15, 2)

weather_description = weather_data["weather"][0].get("description", "Unknown")

# แสดงผล
print(f"เมือง: {city}, ประเทศ: {country}")
print(f"อุณหภูมิ: {temperature}°C, รู้สึกเหมือน: {feels_like}°C")
print(f"อุณหภูมิต่ำสุด: {temp_min}°C, อุณหภูมิสูงสุด: {temp_max}°C")
print(f"สภาพอากาศ: {weather_description}")
