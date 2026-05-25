from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests

from services import fetch_coins
from schemas import CoinsResponse, ErrorResponse, Coin

app = FastAPI(title="Public API Explorer", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get(
    "/api/coins",
    response_model=CoinsResponse,
   
)
def get_coins():
    try:
        data = fetch_coins()
        coins = [Coin(**item) for item in data]
        return CoinsResponse(coins=coins)

    except requests.exceptions.Timeout:
        raise HTTPException(status_code=504, detail="CoinGecko API timed out. Try again.")

    except requests.exceptions.ConnectionError:
        raise HTTPException(status_code=502, detail="Could not reach CoinGecko. Check your connection.")

    except requests.exceptions.HTTPError as e:
        raise HTTPException(status_code=502, detail=f"CoinGecko returned an error: {e.response.status_code}")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")