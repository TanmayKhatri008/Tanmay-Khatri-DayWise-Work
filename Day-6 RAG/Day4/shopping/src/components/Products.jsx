import { useEffect, useState } from "react"

export default function Products({products}) {
    
 
    

    return (
        <div className="products-grid">

            {products.map((product) => (

                <div className="product-card" key={product.id}>

                    <div className="product-image">
                        <img
                            src={product.images[0]}
                            alt={product.title}
                        />
                    </div>

                    <div className="product-info">

                        <h3>{product.title}</h3>

                        <p className="category">
                            {product.category}
                        </p>

                        <h4 className="price">
                            $ {product.price}
                        </h4>

                    </div>

                </div>

            ))}

        </div>
    )
}