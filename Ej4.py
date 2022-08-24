import requests
import json

city = input("Ingrese la ciudad cuya temperatura máxima y mínima desea conocer")
weatherUrl = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=2dffb7db26e8ce2d45d7795039bddf4a'
weatherJson = requests.get(weatherUrl)
weatherJson = weatherJson.json()
print(weatherJson)
clima = weatherJson.pop("main")
print(clima)
min = clima["temp_min"]
max = clima["temp_max"]
print(f'La temperatura mínima para {city.capitalize()} es {min} ºF y la máxima es {max} ºF')