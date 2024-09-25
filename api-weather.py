import json
import requests
import tkinter
from tkinter import messagebox


lat_and_lon =[]
temputer = []


try:
    r = requests.get("http://api.openweathermap.org/geo/1.0/direct?q=London&limit=1&appid=key")
    handle1 = r.json()

except json.decoder.JSONDecodeError:
    print("wrong URL")



else:
    for key in handle1:
        for value in key:

            if type(key[value]) == float:
                lat_and_lon.append(key[value])




try:
    r = requests.get("https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=key".format(lat_and_lon[0],lat_and_lon[1]))
    handle2 = r.json()

except json.decoder.JSONDecodeError:
    print("wrong URL")

else:
    for key in handle1:
        for value in key:

            if type(key[value]) == 'temp_min' or type(key[value]) ==  'temp_max':
                temputer.append(key[value])