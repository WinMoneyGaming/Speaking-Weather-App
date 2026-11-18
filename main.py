import requests
import datetime
import pyttsx3

# Initialize voice assistant
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Enter city
city = input("Enter the name of the city: ")
# Weather API
API_KEY = "68fef74e4cda43e2be6171030263010"
url = "https://api.weatherapi.com/v1/forecast.json"
params = {
    "key": API_KEY,
    "q": city,
    "days": 1
}
response = requests.get(url, params=params)

if response.status_code == 200:
    weatherDict = response.json()
    # Get weather information
    city_name = weatherDict['location']['name']
    temperature = weatherDict['current']['temp_c']
    localtime = weatherDict['location']['localtime']
    day = datetime.datetime.strptime(localtime, '%Y-%m-%d %H:%M').strftime('%A')
    condition = weatherDict['current']['condition']['text']
    humidity = weatherDict['current']['humidity']
    forecast = weatherDict['forecast']['forecastday'][0]['day']
    chance_of_rain = forecast['daily_chance_of_rain']
    will_it_rain = forecast['daily_will_it_rain']
    rain_status = "Yes" if will_it_rain == 1 else "No"

    # Display weather report
    print("\n----- YOUR WEATHER REPORT -----")
    print(f"City: {city_name}")
    print(f"Temperature: {temperature}°C")
    print(f"Local Date and Time: {localtime}")
    print(f"Today is: {day}")
    print(f"Weather Condition: {condition}")
    print(f"Humidity: {humidity}%")
    print(f"Chance of Rain: {chance_of_rain}%")
    print(f"Will it rain? {rain_status}")
    print(f"Thank you!")

    # Voice assistant report
    voice_report = (
        f"Good Morning! Here is the weather report for {city_name}. "
        f"Today is {day}. "
        f"The current temperature is {temperature} degrees Celsius. "
        f"The weather condition is {condition}. "
        f"Humidity is {humidity} percent. "
        f"The chance of rain is {chance_of_rain} percent. "
        f"Will it rain today? {rain_status}."
        f"Thank You!"
    )
    print("\nVoice Assistant: Speaking weather report...")
    speak(voice_report)
else:
    print("Error: City not found or API request failed.")
    speak("Sorry, city not found. Please enter a valid city name.")
