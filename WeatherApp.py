import tkinter as tk
from tkinter import font
import requests

HEIGHT = 600
WIDTH = 700

#api.openweathermap.org/data/2.5/forecast?q={city name},{state code},{country code}&appid={API key}
#15b85eb2cb4e4bf8beb168b6925e9b7e


def get_weather(city):
    weather_key = '15b85eb2cb4e4bf8beb168b6925e9b7e'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params = params)
    weather = response.json()

    label['text'] = format_response(weather)

def format_response(weather):
    try: 
        name = (weather['name'])
        description = (weather['weather'][0]['description'])
        temp = (weather['main']['temp'])

        final_str = 'City: {0} \nConditions: {1} \nTemperature (°C): {2}' .format(name, description, temp)
    except:
        final_str = "There was a problem retrieving that information, we're sorry!"

    return final_str

root = tk.Tk()

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file = 'landscape.png')
img_label = tk.Label(root, image = background_image)
img_label.place(relheight = 1, relwidth = 1)

frame = tk.Frame(root, bg = '#80c1ff', bd = 5)
frame.place(anchor = 'n', relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1)

entry = tk.Entry(frame, font = 40)
entry.place(relheight = 1, relwidth = 0.65)

button = tk.Button(frame, text = 'Get Weather', font = ('Courier', 15), command = lambda: get_weather(entry.get()))
button.place(relx = 0.7, relheight = 1, relwidth = 0.3)

lower_frame = tk.Frame(root, bg = '#80c1ff', bd = 10)
lower_frame.place(anchor = 'n', relx = 0.5, rely = 0.25, relwidth = 0.75, relheight = 0.6)

label = tk.Label(lower_frame, font = ('Courier', 15), anchor = 'nw', justify = 'left', bd = 4)
label.place(anchor = 'n', relx = 0.5, relheight = 1, relwidth = 1)

root.mainloop()