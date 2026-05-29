import React from "react";

const Cart = ({ cart }) => {
  const totalPrice = cart.reduce((total, item) => total + item.price, 0);

  return (
    <div className="container mt-5">
      <h2 className="mb-4">My Cart ({cart.length})</h2>

      {cart.length === 0 ? (
        <h4>Cart is empty</h4>
      ) : (
        <>
          {cart.map((item, index) => (
            <div key={index} className="border p-3 mb-3 rounded">
              <h5>{item.title}</h5>

              <p>₹ {item.price}</p>
            </div>
          ))}

          <div className="mt-4 p-3 border rounded bg-light">
            <h4>Total Price: ₹ {totalPrice.toFixed(2)}</h4>
          </div>
        </>
      )}
    </div>
  );
};

export default Cart;
