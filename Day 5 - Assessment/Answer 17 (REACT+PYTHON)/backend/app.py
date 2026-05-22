from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
from dotenv import load_dotenv
from pydantic import BaseModel
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

api_key = os.getenv("API_KEY")


class Weather(BaseModel):
    name: str
    temp: float
    description: str


@app.route("/weather")
def get_weather():

    try:

        city = request.args.get("city", "Jaipur")
        url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        weather = Weather(
            name=data["location"]["name"],
            temp=data["current"]["temp_c"],
            description=data["current"]["condition"]["text"],
        )

        return jsonify(weather.model_dump())

    except:

        return jsonify({"error": "City not found"}), 500

if __name__ == "__main__":
    app.run(debug=True)
