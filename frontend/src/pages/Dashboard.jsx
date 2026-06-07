import { useEffect, useState } from "react";
import api from "../services/api";

function Dashboard() {

  const [products, setProducts] = useState(0);
  const [customers, setCustomers] = useState(0);
  const [orders, setOrders] = useState(0);

  useEffect(() => {

    loadDashboard();

  }, []);

  const loadDashboard = async () => {

    try {

      const productsResponse =
        await api.get("/products");

      const customersResponse =
        await api.get("/customers");

      const ordersResponse =
        await api.get("/orders");

      setProducts(
        productsResponse.data.length
      );

      setCustomers(
        customersResponse.data.length
      );

      setOrders(
        ordersResponse.data.length
      );

    } catch (error) {

      console.error(error);

    }

  };

  return (
    <div style={{ padding: "30px" }}>

      <h1>Inventory Management System</h1>

      <h2>Dashboard</h2>

      <h3>Products: {products}</h3>

      <h3>Customers: {customers}</h3>

      <h3>Orders: {orders}</h3>

    </div>
  );
}

export default Dashboard;