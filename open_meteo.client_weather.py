import requests
import datetime

# API endpoint and parameters
url = 'https://api.open-meteo.com/v1/forecast'
location = 'YOUR_LOCATION'  # Replace with the desired location
parameters = ['temperature_2m', 'humidity_2m', 'wind_speed_10m', 'sunshine']

# Get current date and time
current_datetime = datetime.datetime.now()

# Build the API query URL
query_params = {
    'latitude': 60.63,  # Replace with the latitude of your location
    'longitude': 26.31,  # Replace with the longitude of your location
    'hourly': 'temperature_2m,humidity_2m,wind_speed_10m,sunshine',
    'date': current_datetime.strftime('%Y-%m-%d'),
    'time': current_datetime.strftime('%H:%M'),
}

# Send the API request
response = requests.get(url, params=query_params)
data = response.json()

# Extract the hourly values
hourly_values = data['hourly']

# Print the values
for hour in hourly_values:
    timestamp = hour['timestamp']
    temperature = hour['temperature_2m']
    humidity = hour['humidity_2m']
    wind_speed = hour['wind_speed_10m']
    sunshine = hour['sunshine']

    print(f"Timestamp: {timestamp}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
    print(f"Sunshine: {sunshine} minutes")
    print("--------------")