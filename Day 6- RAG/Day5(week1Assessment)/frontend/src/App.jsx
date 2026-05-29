import { useState, useEffect } from "react";
import { getCoins } from "./services/api";
import Card from "./components/Card";
import SearchBar from "./components/SearchBar";

export default function App() {
  const [coins, setCoins] = useState([]);
  const [query, setQuery] = useState("");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

useEffect(() => {
  const loadCoins = async () => {
    try {
      setLoading(true)
      const data = await getCoins();
      setCoins(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  loadCoins();
}, []);

  const filtered = coins.filter(
    (c) =>
      c.name.toLowerCase().includes(query.toLowerCase()) ||
      c.symbol.toLowerCase().includes(query.toLowerCase())
  );

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error}</p>;

  return (
    <div className="app">
      <h1>Crypto Prices in Rs</h1>
      <SearchBar query={query} onChange={setQuery} />
      <div className="grid">
        {filtered.map((coin) => (
          <Card key={coin.id} coin={coin} />
        ))}
      </div>
    </div>
  );
}