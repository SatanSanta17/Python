import matplotlib.pyplot as plt 

def plot_weather_forecast(data):
    dates = [entry['date'] for entry in data]
    temperatures = [entry['temperature'] for entry in data]
    plt.figure(figsize=(10, 6))
    plt.plot(dates, temperatures, marker='o', linestyle='-')
    plt.title('Temperature data')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_hourly_weather(data):
    hours = [entry['time'] for entry in data]
    temperatures = [entry['temperature'] for entry in data]
    plt.figure(figsize=(10, 6))
    plt.plot(hours, temperatures, marker='o', linestyle='-')
    plt.title('Temperature data')
    plt.xlabel('Hour')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()