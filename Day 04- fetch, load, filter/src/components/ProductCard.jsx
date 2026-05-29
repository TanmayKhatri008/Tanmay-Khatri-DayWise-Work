import React from "react";

const ProductCard = ({ product, addToCart }) => {
  return (
    <div className="col-md-4 mb-4">
      <div className="card p-3 h-100">
        <img
          src={product.images[0]}
          alt={product.title}
          height="150"
          style={{ objectFit: "contain" }}
        />
        <h5 className="mt-3">
          {product.title.slice(0,25)}
        </h5>
        <p>
          ₹ {product.price}
        </p>
        <button
          className="btn btn-primary"
          onClick={() => addToCart(product)}
        >
          Add To Cart
        </button>
      </div>
    </div>
  );
};

export default ProductCard;