import json
import requests
from tkinter import messagebox
from googletrans import Translator


lat_and_lon =[]



with open ("ISO 639-1.json",'r') as file:
    iso = json.load(file)

# Function wich translate country name in enaglish to natvie
def translate_country_name(name,):
    global country_name
    for country in iso:
        cou = country["English"]

        if cou == name:
            translator = Translator()
            result = translator.translate( text =name, src= 'en', dest=country['alpha2'])
            print(result)
            country_name = result.text
            print (country_name)
            return country_name
            

# Function wich get cords of the country 
def get_latAndlon (link,country,login):

    try:

        r = requests.get(link.format(country,login))
        handle1 = r.json()

    except json.decoder.JSONDecodeError:
        print("wrong URL")


    else:
        for key in handle1:

            for value in key:
 
                if type(key[value]) == float:
                    lat_and_lon.append(key[value])
        return lat_and_lon


# Function wich chcecking the weateher in country
def get_and_showinfo(link,login,messege):
    try:
        r = requests.get(link.format(lat_and_lon[0],lat_and_lon[1],login))
        handle2 = r.json()


    except json.decoder.JSONDecodeError:
        print("wrong URL")

    else:

        for key in handle2:
            try:

                for value in handle2[key]:
                    if key == 'weather':
                        for info in handle2[key][0]:
                            
                            if info == 'description':
                                weather =(handle2[key][0][info])
                    try:

                        if value == "temp":
                            temputer = (handle2[key][value])

                    except:
                        pass
            except:
                pass
        messagebox.showinfo ("Tempeture",'in {} temperature is: {} ° K / {} ° C \n weather is: {} '.format (messege, round(temputer), round(temputer - 273 ), weather))





