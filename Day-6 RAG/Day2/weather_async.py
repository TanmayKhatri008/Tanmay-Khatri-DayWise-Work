
import json

from dotenv  import load_dotenv
import os
import asyncio
import httpx
from pydantic import BaseModel


load_dotenv()
api_key = os.getenv("WEATHER_API_KEY")


class Location(BaseModel):
    name:str
    country:str
    localtime:str

class Condition(BaseModel):
    text:str

class AQI(BaseModel):
    co: float
    no2: float
    o3: float
    so2: float

class Current(BaseModel):
    temp_c: float
    feelslike_c: float
    humidity: float
    wind_kph: float
    wind_dir: str
    air_quality:AQI
    uv: float
    vis_km: float
    pressure_mb: float
    condition: Condition


class Report(BaseModel):
    location: Location
    current: Current


def get_input(message, data_type, validator = None, error_message = "Invalid input"):
    while True:
        try:
            value = data_type(input(message))

            if validator and not validator(value):
                print(error_message)
                continue
            return value
        except:
            print(f"Expected {data_type.__name__}, Try again")


def save_report(report):
    path = f"Day2\\reports\\{report.location.name}.json"
    with open(path, "w") as file:
        json.dump(report.model_dump(), file, indent=4)


def get_city():
    return  get_input("Enter name of city: ", 
    str, 
    lambda x: len(x.strip())>0,
    "Enter a value").strip().capitalize()

def printf(data: Report):
    # Separator for clean layout
    border = "=" * 55
    
    print(f"\n{border}")
    print(f" LIVE WEATHER REPORT: {data.location.name.upper()}, {data.location.country.upper()}")
    print(f" Local Time: {data.location.localtime}")
    print(f"{border}")
    
    # Core Metrics
    print(f" Current Condition : {data.current.condition.text}")
    print(f" Temperature       : {data.current.temp_c}°C")
    print(f" Feels Like        : {data.current.feelslike_c}°C")
    
    # Environment Details
    print(f" Humidity          : {data.current.humidity}%")
    print(f" Wind              : {data.current.wind_kph} km/h ({data.current.wind_dir})")
    print(f" Visibility        : {data.current.vis_km} km")
    print(f" UV Index          : {data.current.uv}")
    
    # Air Quality Metrics (Rounded to 2 decimal places using :.2f)
    print(f"{border}")
    print(f" AIR QUALITY METRICS (µg/m³):")
    print(f" • Carbon Monoxide (CO)  : {data.current.air_quality.co:.2f}")
    print(f" • Nitrogen Dioxide (NO2): {data.current.air_quality.no2:.2f}")
    print(f" • Ozone (O3)            : {data.current.air_quality.o3:.2f}")
    print(f" • Sulfur Dioxide (SO2)  : {data.current.air_quality.so2:.2f}")
    print(f"{border}\n")

async def get_weather(city, client):
    details  = await client.get(
        "http://api.weatherapi.com/v1/current.json",
        params = {"key":api_key,
                  "q":city,
                  "aqi": "yes"
                  }
    )
    
    try:
        details.raise_for_status()
        resp = details.json()
        validated = Report.model_validate(resp)
        return validated
    
    except httpx.HTTPStatusError as err:
        print("Invalid city name.....")

async def get_multiple_cities(cities):
    
    async with httpx.AsyncClient() as client:
        tasks= [get_weather(city, client) for city in cities]
        results = await asyncio.gather(*tasks)
    for result in results:
        if result is  not None:
            printf(result)
            save_report(result)
    







details = '''
=================Welcome to weather application=====================
1. See current weather details of a city
2. See current weather reports of multiple cities
3. Exit
'''

while True:
    print(details)

    choice = get_input(
        "Enter your choice: ",
        int,
        lambda x :0<x<4,
        "Enter correct choice"
    )

    if choice == 1:
        city = get_city()
        asyncio.run(get_multiple_cities([city]))

    elif choice == 2:
        num = get_input(
            "Enter number of cities:",
            int,
            lambda x: x>0,
            "Enter a positive number..."
        )
        cities = [get_city() for _ in range(num)]
        asyncio.run(get_multiple_cities(cities))

    elif choice == 3:
        print("Thank you for using !!!")
        break