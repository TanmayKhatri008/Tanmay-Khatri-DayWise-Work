from pydantic import BaseModel
from typing import Optional


class Coin(BaseModel):
    id: str
    symbol: str
    name: str
    image: str
    current_price: float
    market_cap: float
    market_cap_rank: Optional[int]
    price_change_percentage_24h: Optional[float]
    total_volume: Optional[float]       
    circulating_supply: Optional[float]


class CoinsResponse(BaseModel):
    coins: list[Coin]


class ErrorResponse(BaseModel):
    detail: str