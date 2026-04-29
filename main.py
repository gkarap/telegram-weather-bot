import requests
import os


# API configuration
owm_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.getenv("OWM_API_KEY")
bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
chat_id = os.getenv("TELEGRAM_CHAT_ID")

user_name = os.getenv("USER_NAME") # Personal name variable for name in telegram message

def send_telegram_msg(text):
    """Sends a formatted message to Telegram."""
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    
    params = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown" # We use parse_mode='Markdown' to allow bold text and emojis
    }
    response = requests.get(url, params=params)
    response.raise_for_status()

# Request parameters (this example is for Athens, Greece)
weather_params = {
    "lat": "37.983810", #latitude
    "lon": "23.727539", #longitude
    "appid": api_key,
    "units": "metric",
    "cnt": 4, # Checking the next 12 hours
}

response = requests.get(owm_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
will_be_windy = False
temperatures = []
wind_threshold = 8.0 

# Data Processing Loop
for hour_data in weather_data["list"]:
    # 1. Temperature data
    temp = hour_data["main"]["temp"]
    temperatures.append(temp)
    
    # 2. Precipitation check (Codes < 800)
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 800:
        will_rain = True
        
    # 3. Wind speed check
    wind_speed = hour_data["wind"]["speed"]
    if wind_speed > wind_threshold:
        will_be_windy = True

# Calculations
avg_temp = sum(temperatures) / len(temperatures)
min_temp = min(temperatures)
max_temp = max(temperatures)

# Formatting Status Strings
if will_rain:
    rain_status = "is expected ☔" 
else:
    rain_status = "is not expected ☀️"

if will_be_windy:
    wind_status = "High winds expected! 💨"
else:
    wind_status = "Normal"

# Constructing the final message as a Dashboard
final_message = (
    f" *Good morning {user_name} !*\n"
    f"Your personal weather report:\n\n"
    f"  *Temperature:* {min_temp:.1f}°C - {max_temp:.1f}°C \n"
    f"    (Avg: {avg_temp:.1f}°C)\n"
    f"  *Rain:* {rain_status}\n"
    f"  *Wind:* {wind_status}\n\n"
    f" Have a productive day !"
)

send_telegram_msg(final_message)

