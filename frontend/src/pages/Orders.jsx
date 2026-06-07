import { useEffect, useState } from "react";
import api from "../services/api";

function Orders() {

  const [orders, setOrders] = useState([]);

  const [formData, setFormData] = useState({
    customer_id: "",
    product_id: "",
    quantity: ""
  });

  useEffect(() => {
    loadOrders();
  }, []);

  const loadOrders = async () => {

    const response =
      await api.get("/orders");

    setOrders(response.data);

  };

  const handleChange = (e) => {

    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });

  };

  const createOrder = async () => {
  if (!formData.customer_id) {
  alert("Customer ID is required");
  return;
}

if (Number(formData.customer_id) <= 0) {
  alert("Customer ID must be greater than 0");
  return;
}

if (!formData.product_id) {
  alert("Product ID is required");
  return;
}

if (Number(formData.product_id) <= 0) {
  alert("Product ID must be greater than 0");
  return;
}

if (!formData.quantity) {
  alert("Quantity is required");
  return;
}

if (Number(formData.quantity) <= 0) {
  alert("Quantity must be greater than 0");
  return;
}

    try {

      await api.post(
        "/orders",
        {
          customer_id:
            Number(formData.customer_id),

          product_id:
            Number(formData.product_id),

          quantity:
            Number(formData.quantity)
        }
      );

      setFormData({
        customer_id: "",
        product_id: "",
        quantity: ""
      });

      loadOrders();

    } catch (error) {

      alert(
        error.response?.data?.detail ||
        "Failed to create order"
      );

    }

  };

  return (
    <div style={{ padding: "20px" }}>

      <h1>Orders</h1>

      <div
        style={{
          display: "flex",
          gap: "10px",
          flexWrap: "wrap",
          marginBottom: "20px"
        }}
      >

        <input
          name="customer_id"
          placeholder="Customer ID"
          value={formData.customer_id}
          onChange={handleChange}
        />

        <input
          name="product_id"
          placeholder="Product ID"
          value={formData.product_id}
          onChange={handleChange}
        />

        <input
          name="quantity"
          placeholder="Quantity"
          value={formData.quantity}
          onChange={handleChange}
        />

        <button
          onClick={createOrder}
          style={{
            background: "blue",
            color: "white",
            border: "none",
            padding: "10px 20px",
            borderRadius: "5px"
          }}
        >
          Create Order
        </button>

      </div>

      <table border="1">

        <thead>
          <tr>
            <th>ID</th>
            <th>Customer ID</th>
            <th>Product ID</th>
            <th>Quantity</th>
            <th>Total Amount</th>
          </tr>
        </thead>

        <tbody>

          {orders.map(order => (

            <tr key={order.id}>
              <td>{order.id}</td>
              <td>{order.customer_id}</td>
              <td>{order.product_id}</td>
              <td>{order.quantity}</td>
              <td>{order.total_amount}</td>
            </tr>

          ))}

        </tbody>

      </table>

    </div>
  );
}

export default Orders;
