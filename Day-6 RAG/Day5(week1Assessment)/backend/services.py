import os
import requests


COINGECKO_BASE_URL = "https://api.coingecko.com/api/v3"


def fetch_coins() -> list[dict]:
    url = f"{COINGECKO_BASE_URL}/coins/markets"
    params = {
        "vs_currency": "inr",
        "order": "market_cap_desc",
        "per_page": 100,
        "page": 1,
        "sparkline": False,
        "price_change_percentage": "24h",
    }
    headers = {
        "accept": "application/json",
        
    }

    response = requests.get(url, params=params, headers=headers, timeout=10)
    response.raise_for_status()
    return response.json()