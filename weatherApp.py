##jpappy973
##weather gui

import tkinter as tk
from tkinter import font
import requests

height=500
width=600

def test_function(entry):
    print("buttin clicked", entry)

# api.openweathermap.org/data/2.5/forecast?q={city name}&appid={your api key}
# dbb7d5d9342a78b94d44da9812526a29

def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        ctemp = int((temp-32)*5/9)
        wind = weather['main']['humidity']
        min_temp = weather['main']['temp_min']
        max_temp = weather['main']['temp_max']

        final_str = 'City: %s \nConditions: %s \nTemperture (℉): %s \nTemperture (°C):%s \nMinimum Temperture: %s \nMaximum Temperture: %s \nHumidity: %s ' % (name, desc, int(temp),ctemp, int(min_temp), int(max_temp), wind)
    except:
        final_str = 'check spelling.'
    print(ctemp)
    return final_str


def get_weather(city):
    weather_key = 'dbb7d5d9342a78b94d44da9812526a29'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()

    print(response)
    label['text'] = format_response(weather)





root = tk.Tk()

canvas =tk.Canvas(root, height=height, width=width)
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#b3e7ff', bd=5)
frame.place(relx=0.45, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=('ino', 17))
entry.place(relwidth=0.75, relheight=1)

button = tk.Button(frame, text="Get Weather", font=('ino', 15), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='#b3e7ff', bd=5)
lower_frame.place(relx=0.45, rely=0.20, relwidth=0.75, relheight=0.7, anchor='n')


label = tk.Label(lower_frame, font=('ino', 20))
label.place( relwidth=1, relheight=1)


root.mainloop()

