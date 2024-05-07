import tkinter as tk
from API_fetch import get_current_weather, get_weather_forecast, get_hourly_weather
from main import display_current_weather, display_wether_forcast, display_hourly_wether

def fetch_current_weather():
    city = city_entry.get()
    display_current_weather(city)

def fetch_weather_forecast():
    city = city_entry.get()
    display_wether_forcast(city)

def fetch_hourly_weather():
    city = city_entry.get()
    display_hourly_wether(city)


# Create main window
window = tk.Tk()
window.title("Weather Forecast App")

# Create input field for city name
city_label = tk.Label(window, text="Enter City Name:")
city_label.pack()
city_entry = tk.Entry(window)
city_entry.pack()

# Create buttons for fetching weather data
current_weather_button = tk.Button(window, text="Fetch Current Weather", command=fetch_current_weather)
current_weather_button.pack()

weather_forecast_button = tk.Button(window, text="Fetch Weather Forecast", command=fetch_weather_forecast)
weather_forecast_button.pack()

hourly_weather_button = tk.Button(window, text="Fetch Hourly Weather", command=fetch_hourly_weather)
hourly_weather_button.pack()

# Create text widget for displaying weather data
display_text = tk.Label(window, text="")
display_text.pack()

# Run the main event loop
window.mainloop()
