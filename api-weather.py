import json
import requests
import tkinter as tk
from tkinter import messagebox


Key = "XXX"
lat_and_lon =[]
temputer = []
root = tk.Tk()
root.title("In wich country you want chek tempeture")


def cheking_country():
    global messeg
    messeg = input_text.get()
    if not messeg.strip():
        messagebox.showwarning("error", "pleas give name of country")
        return  
    else:
        root.destroy()

    
    
    

label =tk.Label(root, text="Wirte name of the country in wich you want chek temeprature:")
label.pack(padx=10, pady=10)
input_text = tk.Entry(root, width=40)
input_text.pack(padx=10, pady=10)
button = tk.Button(root, text="check tempeture ", command=cheking_country)
button.pack(padx=10, pady=10)
root.mainloop()



try:
    r = requests.get("http://api.openweathermap.org/geo/1.0/direct?q={}&limit=1&appid={}".format(messeg.capitalize(),Key))
    handle1 = r.json()

except json.decoder.JSONDecodeError:
    print("wrong URL")



else:
    for key in handle1:
        for value in key:
            

            if type(key[value]) == float:
                lat_and_lon.append(key[value])




try:
    r = requests.get("https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}".format(lat_and_lon[0],lat_and_lon[1],Key))
    handle2 = r.json()


except json.decoder.JSONDecodeError:
    print("wrong URL")

else:

    for key in handle2:
        try:
            print(handle2[key])

            for value in handle2[key]:
                try:
                    print(handle2[key][value])
                except:
                    pass
        except:
            pass

        

            
    messagebox.showinfo ("Tempeture", temputer)