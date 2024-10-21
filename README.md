# weather_task
**Features**
Real-time Data Collection: Automatically collects weather data for cities every 5 minutes.
Daily Weather Summaries: Aggregates data to calculate daily averages for temperature, humidity, and wind speed.
Threshold-Based Alerts: Triggers alerts if the temperature exceeds a user-defined threshold for two consecutive updates.
Visualizations: Plots daily weather trends, including average temperature and humidity, using matplotlib.
**Technologies Used**
Python 3.x: Programming language used to build the system.
OpenWeatherMap API: Provides real-time weather data.
Requests: Python library to make HTTP requests to the OpenWeatherMap API.
Matplotlib: Python library used for plotting weather trends.

Collections (Counter): For counting the most frequent weather conditions.

**Prerequisites**
Python 3.x installed on your machine.
OpenWeatherMap API Key (You can get it here).

**Install the required Python dependencies:**
pip install -r requirements.txt
API Key: Replace the API_KEY variable with your own API key from OpenWeatherMap.

Update Interval: The default interval to fetch new weather data is 5 minutes (300 seconds). You can modify the INTERVAL variable to change this:


INTERVAL = 300  # Time in seconds between each API call
Temperature Threshold: To configure the temperature threshold for alerts, update the THRESHOLD variable:

THRESHOLD = 35  # Celsius temperature for alert threshold
The system continuously collects weather data and processes it into daily summaries for the six metro cities in India: Delhi, Mumbai, Chennai, Bangalore, Kolkata, and Hyderabad. The collected weather data includes:

Temperature (Celsius)
Humidity (%)
Wind speed (meters/second)
Main weather condition (e.g., Clear, Rain, Clouds)
The script calculates daily aggregates and shows:

Average temperature
Average humidity
Average wind speed
Dominant weather condition
