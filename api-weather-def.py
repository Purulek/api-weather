import json
import requests
import tkinter as tk
from tkinter import messagebox
from googletrans import Translator





Key = "XXX"
lat_and_lon =[]
link_lat = "http://api.openweathermap.org/geo/1.0/direct?q={}&limit=1&appid={}"


root = tk.Tk()
root.title("In wich country you want chek tempeture")


with open ("ISO 639-1.json",'r') as file:
    iso = json.load(file)

    
def cheking_country():
    global messeg
    messeg = input_text.get()
    if not messeg.strip():
        messagebox.showwarning("error", "pleas give name of country")
        return  
    else:
        root.destroy()


def translate_country_name(name):
    global country_name
    for country in iso:
        cou = country["English"]

        if cou == name:
            print(cou)
            translator = Translator()
            result = translator.translate( text =name, src= 'en', dest=country['alpha2'])
            country_name = result.text
            
def label_weather():
    global input_text
    
    label =tk.Label(root, text="Wirte name of the country in wich you want chek temeprature:")
    label.pack(padx=10, pady=10)
    input_text = tk.Entry(root, width=40)
    input_text.pack(padx=10, pady=10)
    button = tk.Button(root, text="check tempeture ", command= cheking_country)
    button.pack(padx=10, pady=10)
    
    root.mainloop()
    


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



def get_and_showinfo():
    try:
        r = requests.get("https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}".format(lat_and_lon[0],lat_and_lon[1],Key))
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

        messagebox.showinfo ("Tempeture",'in {} temperature is: {} ° K / {} ° C \n weather is: {} '.format (messeg, round(temputer), round(temputer - 273 ), weather))



label_weather()

translate_country_name(messeg)

get_latAndlon(link_lat,country_name,Key)

