import React from "react";
import ProductCard from "./ProductCard";

const Products = ({ products, loading, addToCart, search }) => {
  const filteredProducts = products.filter((product) =>
    product.title.toLowerCase().includes((search || "").toLowerCase()),
  );

  if (loading) {
    return (
      <div className="text-center mt-5">
        <div className="spinner-border" role="status"></div>

        <h4 className="mt-3">Loading Products...</h4>
      </div>
    );
  }

  return (
    <div className="container mt-4">
      <div className="row">
        {filteredProducts.slice(0, 12).map((product) => (
          <ProductCard
            key={product.id}
            product={product}
            addToCart={addToCart}
          />
        ))}
      </div>
    </div>
  );
};

export default Products;
