import { useEffect, useState } from "react";
import Filter from "./components/Filter";
import Hero from "./components/Hero";
import Navbar from "./components/Navbar";
import Products from "./components/Products";
import Empty from "./components/Empty";
import Loading from "./components/Loading";

export default function HomePage() {

    const [products, setProducts] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");
    const [selectedCat, setSelectedCat] = useState("all");
    const [search, setSearch] = useState("")

  

    useEffect(() => {
        async function fetchProds() {
            setLoading(true);
            setError("");
            try {
                const response = await fetch('https://dummyjson.com/products?limit=0');

                if (!response.ok) {
                    throw new Error("Failed to fetch product");
                }

                const data = await response.json()
                setProducts(data.products)
            } catch (err) {
                setError(err.message);
            } finally {
                setLoading(false);
            }


        };


        fetchProds();
    }, []);
      
      
      const filteredProds = products.filter(
        prod=>{
          const catm = selectedCat === "all" || prod.category === selectedCat;

          const searchm = prod.title.toLowerCase().includes(search.toLowerCase());

          return (catm && searchm) ;

        }
      );

      const categories = [
    "all",
    ...new Set(
        products.map(
            (prod) => prod.category
        )
    )
];

  return (
    <div className="app">

      {/* NAVBAR */}
        <Navbar />      

      {/* HERO SECTION */}
       <Hero 
        search = {search}
        setSearch = {setSearch}
       />

      {/* FILTER SECTION */}
        <Filter 
            selectedCat = {selectedCat}
            setSelectedCat = {setSelectedCat}
            categories = {categories}
            />


      {loading? 
        <Loading />: 
        (filteredProds.length === 0?
          <Empty /> :
          <Products 
            products = {filteredProds}
          />
        ) 
      }

    </div>
  );
}