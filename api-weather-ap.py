import api_weather_def as wh 

Key = "XXX"
lat_and_lon =[]
link_lat = "http://api.openweathermap.org/geo/1.0/direct?q={}&limit=1&appid={}"
link_temp = "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}"
messeg = ""
country_name = ""

wh.label_weather()

wh.translate_country_name(messeg)

wh.get_latAndlon(link_lat,country_name,Key)

wh.get_and_showinfo(link_temp, Key)