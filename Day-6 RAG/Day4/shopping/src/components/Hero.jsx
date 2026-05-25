export default function Hero({search, setSearch})
{
    return(
        <section className="hero">
        <h2>Discover Products Easily</h2>

        <p>
          Browse products from multiple categories
        </p>

        <input
          type="text"
          placeholder="Search products..."
          className="search-box"
          value = {search}
          onChange={(event)=>setSearch(event.target.value)}
        />
      </section>
    )
}