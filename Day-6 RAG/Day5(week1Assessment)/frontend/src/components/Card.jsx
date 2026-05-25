export default function Card({ coin }) {
  const isPositive = coin.price_change_percentage_24h >= 0;

  return (
    <div className="card">
      <img src={coin.image} alt={coin.name} width={40} height={40} />
      <div className="card-info">
        <h3>{coin.name} <span className="symbol">{coin.symbol.toUpperCase()}</span></h3>
        <p className="price">₹{coin.current_price?.toLocaleString("en-IN")}</p>
        <p className="market-cap">MCap: ₹{coin.market_cap?.toLocaleString("en-IN")}</p>
      </div>
      <div className={`change ${isPositive ? "positive" : "negative"}`}>
        {isPositive ? "▲" : "▼"} {Math.abs(coin.price_change_percentage_24h).toFixed(2)}%
      </div>
    </div>
  );
}