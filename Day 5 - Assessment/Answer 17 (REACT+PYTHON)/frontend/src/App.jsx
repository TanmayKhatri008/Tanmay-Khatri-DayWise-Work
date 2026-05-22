import { useState } from "react";
import Card from "./components/Card";
import "./App.css";

function App() {
  const [search, setSearch] = useState("");
  const [weather, setWeather] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function fetchWeather() {
    setLoading(true);
    setError("");

    try {
      const response = await fetch(
        `http://127.0.0.1:5000/weather?city=${search}`,
      );

      const data = await response.json();

      if (data.error) {
        setError(data.error);
      } else {
        setWeather(data);
      }
    } catch {
      setError("Failed to fetch");
    }

    setLoading(false);
  }

  return (
    <div className="container">
      <h1>Weather App</h1>

      <input
        type="text"
        placeholder="Enter city..."
        value={search}
        onChange={(e) => setSearch(e.target.value)}
      />

      <button onClick={fetchWeather}>Search</button>

      {loading && <h2>Loading...</h2>}

      {error && <h2>{error}</h2>}

      {weather && (
        <Card
          city={weather.name}
          temp={weather.temp}
          description={weather.description}
        />
      )}
    </div>
  );
}

export default App;
