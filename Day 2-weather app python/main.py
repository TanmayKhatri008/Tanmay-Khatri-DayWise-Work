import requests
import os
import json
import time
from datetime import datetime
from pydantic import BaseModel, ValidationError
from dotenv import load_dotenv
from typing import Optional

load_dotenv()

app_name = os.getenv("APP_NAME", "Weather App")
api_key = os.getenv("API_KEY")

print(f"{app_name} shuru ho rha h.....")

time.sleep(1)


class Condition(BaseModel):
    text: str


class Current(BaseModel):
    temp_c: float
    humidity: int
    feelslike_c: float
    condition: Condition


class Location(BaseModel):
    name: str
    country: str


class WeatherResponse(BaseModel):
    location: Location
    current: Current


def fetch_weather(city):
    url = "http://api.weatherapi.com/v1/current.json"
    params = {"key": api_key, "q": city}
    try:
        print(f"fetching weather...\n")
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        weather = WeatherResponse(**data)
        return weather

    except requests.exceptions.ConnectionError:
        print("No internet connection")

    except requests.exceptions.Timeout:
        print("There is a timeout ")

    except requests.exceptions.HTTPError as e:
        print(f"HTTP error {e}")

    except Exception as e:
        print(f"Unexpected error: {e}")

    return None


def analyze_current_weather(weather):
    summary = {
        "city": weather.location.name,
        "country": weather.location.country,
        "temperature": weather.current.temp_c,
        "humidity": weather.current.humidity,
        "feels_like": weather.current.feelslike_c,
        "condition": weather.current.condition.text,
        "generated_time": datetime.now(),
    }
    return summary


def write_report(summary):
    with open("report.json", "a", encoding="utf-8") as f:
        json.dump(summary, f, indent=4, default=str)
    print("save ho gyaaaa woh bhi json m")


def main():
    city = input("Enter your city - ")
    weather = fetch_weather(city)
    if weather:
        summary = analyze_current_weather(weather)
        write_report(summary)
        print("\n Generated the summary \n")
        print(json.dumps(summary, indent=4, default=str))


if __name__ == "__main__":
    main()
