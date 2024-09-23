import json
import requests
import tkinter


lat_and_lon =[]

try:
    r = requests.get("http://api.openweathermap.org/geo/1.0/direct?q=London&limit=1&appid=key")
    handle1 = r.json()

except json.decoder.JSONDecodeError:
    print("wrong URL")

for key in handle1:
    print("-"*20)
    for value in key:

        if type(key[value]) == float:
            lat_and_lon.append(key[value])




try:
    r = requests.get("https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=key".format(lat_and_lon[0],lat_and_lon[1]))
    handle2 = r.json()

except json.decoder.JSONDecodeError:
    print("wrong URL")

else:
    print(handle2)