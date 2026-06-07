import { useEffect, useState } from "react";
import api from "../services/api";

function Products() {

  const [products, setProducts] = useState([]);

  const [formData, setFormData] = useState({
    name: "",
    sku: "",
    price: "",
    quantity: ""
  });

  useEffect(() => {
    loadProducts();
  }, []);

  const loadProducts = async () => {

    const response =
      await api.get("/products");

    setProducts(response.data);

  };

  const handleChange = (e) => {

    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });

  };

  const createProduct = async () => {
  if (!formData.name.trim()) {
  alert("Product name is required");
  return;
}

if (!/^[A-Za-z ]+$/.test(formData.name)) {
  alert("Product name should contain only letters");
  return;
}

if (!formData.sku.trim()) {
  alert("SKU is required");
  return;
}

if (!/^[A-Za-z0-9]+$/.test(formData.sku)) {
  alert("SKU should contain only letters and numbers");
  return;
}

if (!formData.price.trim()) {
  alert("Price is required");
  return;
}

if (isNaN(formData.price)) {
  alert("Price must be a valid number");
  return;
}

if (Number(formData.price) <= 0) {
  alert("Price must be greater than 0");
  return;
}

if (!formData.quantity.trim()) {
  alert("Quantity is required");
  return;
}

if (isNaN(formData.quantity)) {
  alert("Quantity must be a valid number");
  return;
}

if (Number(formData.quantity) < 0) {
  alert("Quantity cannot be negative");
  return;
}
    try {

      await api.post(
        "/products",
        {
          ...formData,
          price: Number(formData.price),
          quantity: Number(formData.quantity)
        }
      );

      setFormData({
        name: "",
        sku: "",
        price: "",
        quantity: ""
      });

      loadProducts();

    }
    catch (error) {

  const detail =
    error.response?.data?.detail;

  if (Array.isArray(detail)) {

    alert(detail[0].msg);

  } else {

    alert(detail);

  }

}
  };

  return (
    <div style={{ padding: "20px" }}>

      <h1>Products</h1>

      <div
        style={{
          display: "flex",
          gap: "10px",
          flexWrap: "wrap",
          marginBottom: "20px"
        }}
      >

        <input
          name="name"
          placeholder="Product Name"
          value={formData.name}
          onChange={handleChange}
        />

        <input
          name="sku"
          placeholder="SKU"
          value={formData.sku}
          onChange={handleChange}
        />

        <input
          name="price"
          placeholder="Price"
          value={formData.price}
          onChange={handleChange}
        />

        <input
          name="quantity"
          placeholder="Quantity"
          value={formData.quantity}
          onChange={handleChange}
        />

        <button
          onClick={createProduct}
          style={{
            background: "blue",
            color: "white",
            border: "none",
            padding: "10px 20px",
            borderRadius: "5px"
          }}
        >
          Create Product
        </button>

      </div>

      <table border="1">

        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>SKU</th>
            <th>Price</th>
            <th>Quantity</th>
          </tr>
        </thead>

        <tbody>

          {products.map(product => (

            <tr key={product.id}>
              <td>{product.id}</td>
              <td>{product.name}</td>
              <td>{product.sku}</td>
              <td>{product.price}</td>
              <td>{product.quantity}</td>
            </tr>

          ))}

        </tbody>

      </table>

    </div>
  );
}

export default Products;

