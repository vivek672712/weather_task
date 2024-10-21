import requests
import time
from collections import Counter
import matplotlib.pyplot as plt
 
API_KEY = 'ddc032fd6552c33f3ddf93b3083a8ae1'  
CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
INTERVAL = 300
THRESHOLD = 35  
DAILY_WEATHER_DATA = {}  
DAILY_SUMMARIES = {}  
 
def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()
        return parse_weather_data(data, city)
    except requests.RequestException as e:
        print(f"Error fetching data for {city}: {e}")
        return None
 
def parse_weather_data(data, city):
    kelvin_temp = data['main']['temp']
    return {
        'city': city,
        'temp': kelvin_temp - 273.15,  
        'humidity': data['main']['humidity'],
        'wind_speed': data['wind']['speed'],
        'weather': data['weather'][0]['main'],
        'timestamp': data['dt']
    }
 
def collect_weather_data():
    global DAILY_WEATHER_DATA
    for city in CITIES:
        weather_data = get_weather_data(city)
        if weather_data:
            print(f"Collected weather data for {city}: {weather_data}")
            if city not in DAILY_WEATHER_DATA:
                DAILY_WEATHER_DATA[city] = []
            DAILY_WEATHER_DATA[city].append(weather_data)
 
def calculate_daily_summary(weather_data):
    temps = [entry['temp'] for entry in weather_data]
    humidities = [entry['humidity'] for entry in weather_data]
    wind_speeds = [entry['wind_speed'] for entry in weather_data]
    weather_conditions = [entry['weather'] for entry in weather_data]
 
    avg_temp = sum(temps) / len(temps)
    avg_humidity = sum(humidities) / len(humidities)
    avg_wind_speed = sum(wind_speeds) / len(wind_speeds)
 
    dominant_condition = Counter(weather_conditions).most_common(1)[0][0]
 
    return {
        'avg_temp': avg_temp,
        'avg_humidity': avg_humidity,
        'avg_wind_speed': avg_wind_speed,
        'dominant_weather': dominant_condition
    }
 
def check_for_alerts(city, weather_data, threshold):
    consecutive_count = 0
    for entry in weather_data:
        if entry['temp'] > threshold:
            consecutive_count += 1
        else:
            consecutive_count = 0
        
        if consecutive_count >= 2:
            print(f"Alert! In {city}, temperature exceeded {threshold}°C for two consecutive updates.")
            break
 
def plot_weather_trends(daily_summaries, city):
    dates = list(range(1, len(daily_summaries) + 1))
    avg_temps = [entry['avg_temp'] for entry in daily_summaries]
    avg_humidities = [entry['avg_humidity'] for entry in daily_summaries]
 
    plt.figure(figsize=(10, 5))
    plt.plot(dates, avg_temps, label="Average Temperature (°C)", marker='o')
    plt.plot(dates, avg_humidities, label="Average Humidity (%)", linestyle=':', marker='x')
 
    plt.xlabel("Days")
    plt.ylabel("Values")
    plt.title(f"Daily Weather Trends for {city}")
    plt.legend()
    plt.grid()
    plt.show()
 
def main():
    while True:
        print("Collecting weather data...")
        collect_weather_data()
        time.sleep(INTERVAL)
        
        for city, weather_data in DAILY_WEATHER_DATA.items():
            summary = calculate_daily_summary(weather_data)
            print(f"Daily Summary for {city}: {summary}")
            
            
            if city not in DAILY_SUMMARIES:
                DAILY_SUMMARIES[city] = []
            DAILY_SUMMARIES[city].append(summary)
            
            check_for_alerts(city, weather_data, THRESHOLD)
        
        
        for city, summaries in DAILY_SUMMARIES.items():
            plot_weather_trends(summaries, city)
 
        DAILY_WEATHER_DATA.clear()  
 
if __name__ == "__main__":
    main()