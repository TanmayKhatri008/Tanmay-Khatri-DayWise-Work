const BASE_URL = "https://supreme-space-fishstick-5vqw97g7xq54h74g6-8000.app.github.dev";

export async function getCoins() {
  const response = await fetch(`${BASE_URL}/api/coins`);
  if (!response.ok) {
    const err = await response.json();
    throw new Error(err.detail || "Failed to fetch coins");
  }
  const data = await response.json();
  return data.coins;
}