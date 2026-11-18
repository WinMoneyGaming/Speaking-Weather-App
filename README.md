# 🌦️ Speaking Weather App – Python Voice Assistant

A Python-based Weather Application that provides real-time weather information for any city worldwide and converts weather updates into speech using a Text-to-Speech (TTS) voice assistant.

The application fetches weather data using the **WeatherAPI** and delivers both textual and voice-based weather reports.

## 🚀 Features

- 🌍 **City-Based Weather Search:** Get weather information by entering any city name.
- 🌡️ **Current Temperature:** Displays current temperature in Celsius.
- 📅 **Local Date & Time:** Shows the local date and time of the selected city.
- ☁️ **Weather Conditions:** Displays current weather conditions.
- 💧 **Humidity Information:** Provides current humidity percentage.
- 🌧️ **Rain Forecast:** Displays the probability of rain.
- ☔ **Rain Prediction:** Indicates whether rain is expected (Yes/No).
- 🔊 **Voice Assistant:** Reads the complete weather report aloud using Python Text-to-Speech.
- ⚠️ **Error Handling:** Handles invalid city names and API request failures.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Requests | API requests and data retrieval |
| WeatherAPI | Real-time weather and forecast data |
| JSON | Processing API responses |
| DateTime | Local date and day calculation |
| pyttsx3 | Text-to-Speech voice assistant |

## 📂 Project Structure

```text
Speaking-Weather-App/
│
├── weather.py
├── README.md
├── requirements.txt
└── .gitignore
```

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/WinMoneyGaming/Speaking-Weather-App.git
```

### 2. Navigate to the project directory

```bash
cd Speaking-Weather-App
```

### 3. Install required libraries

```bash
pip install -r requirements.txt
```

### 4. Configure WeatherAPI

- Visit https://www.weatherapi.com/
- Create an account and generate your API key.
- Store your API key securely using an environment variable.

Example:

```python
import os

API_KEY = os.getenv("WEATHER_API_KEY")
```

Set the environment variable before running the application.

### 5. Run the application

```bash
python weather.py
```

## 💻 Sample Output

```text
Enter the name of the city: Chandigarh

----- YOUR WEATHER REPORT -----

City: Chandigarh
Temperature: 25°C
Local Date and Time: 2026-11-18 14:30
Today is: Wednesday
Weather Condition: Partly cloudy
Humidity: 60%
Chance of Rain: 20%
Will it rain? No

Voice Assistant: Speaking weather report...
```

*Note: Sample weather values are illustrative and will vary according to live API data.*

## 🔊 Voice Assistant

The application uses the `pyttsx3` library to convert the weather report into spoken output.

The voice assistant reads:
- City name
- Current temperature
- Weather conditions
- Humidity
- Chance of rain
- Rain prediction

## 📦 Requirements

Create a `requirements.txt` file:

```text
requests
pyttsx3
```

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

- Python programming and functions.
- Working with third-party REST APIs.
- JSON data extraction and manipulation.
- Handling API responses and errors.
- Implementing Text-to-Speech technology.
- Building a real-world Python application.

## 🔮 Future Improvements

- Voice input to search cities using speech recognition.
- Hindi and multilingual voice support.
- Graphical User Interface (GUI) using Tkinter.
- Extended 7-day weather forecasts.
- Interactive voice-based weather queries.

## 👨‍💻 Developer

**WinMoneyGaming**

GitHub Repository: https://github.com/WinMoneyGaming/Speaking-Weather-App

---

⭐ If you find this project useful, consider giving it a star!

**Feedback and suggestions are always welcome.**
