import api_weather_def as wh 
import tkinter as tk
from tkinter import messagebox

Key = "XXX"

link_lat = "http://api.openweathermap.org/geo/1.0/direct?q={}&limit=1&appid={}"
link_temp = "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}"


root = tk.Tk()
root.title("In wich country you want chek tempeture")

def cheking_country():
    global messeg
    messeg = input_text.get()
    if not messeg.strip():
        messagebox.showwarning("error", "pleas give name of country")
    else:
        root.destroy()

def label_weather():
    global input_text
    label =tk.Label(root, text="Wirte name of the country in wich you want chek temeprature:")
    label.pack(padx=10, pady=10)
    input_text = tk.Entry(root, width=40)
    input_text.pack(padx=10, pady=10)
    button = tk.Button(root, text="check tempeture ", command= cheking_country)
    button.pack(padx=10, pady=10)
    root.mainloop()



label_weather()



country_name = wh.translate_country_name(messeg)

lat_and_lon = wh.get_latAndlon(link_lat,country_name,Key)

wh.get_and_showinfo(link_temp, Key, messeg)





