function Card({ city, temp, description }) {
  return (
    <div className="card">
      <h1>{city}</h1>

      <h2>{temp}°C</h2>

      <p>{description}</p>
    </div>
  );
}

export default Card;
