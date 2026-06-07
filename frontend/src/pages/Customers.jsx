import { useEffect, useState } from "react";
import api from "../services/api";

function Customers() {

  const [customers, setCustomers] = useState([]);

  const [formData, setFormData] = useState({
    full_name: "",
    email: "",
    phone_number: ""
  });

  useEffect(() => {
    loadCustomers();
  }, []);

  const loadCustomers = async () => {

    const response =
      await api.get("/customers");

    setCustomers(response.data);

  };

  const handleChange = (e) => {

    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });

  };

  const createCustomer = async () => {
  if (!formData.full_name.trim()) {
  alert("Full name is required");
  return;
}

if (!/^[A-Za-z ]+$/.test(formData.full_name)) {
  alert("Name should contain only letters");
  return;
}

if (!formData.email.trim()) {
  alert("Email is required");
  return;
}

const emailRegex =
  /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

if (!emailRegex.test(formData.email)) {
  alert("Enter a valid email address");
  return;
}

if (!formData.phone_number.trim()) {
  alert("Phone number is required");
  return;
}

if (!/^[0-9]{10}$/.test(formData.phone_number)) {
  alert("Phone number must be 10 digits");
  return;
}

    try {

      await api.post(
        "/customers",
        formData
      );

      setFormData({
        full_name: "",
        email: "",
        phone_number: ""
      });

      loadCustomers();

    }
    catch (error) {

      alert(
        error.response?.data?.detail ||
        "Failed to create customer"
      );

    }

  };

  return (
    <div style={{ padding: "20px" }}>

      <h1>Customers</h1>

      <div
        style={{
          marginBottom: "20px",
          display: "flex",
          gap: "10px",
          flexWrap: "wrap"
        }}
      >

        <input
          type="text"
          name="full_name"
          placeholder="Full Name"
          value={formData.full_name}
          onChange={handleChange}
        />

        <input
          type="email"
          name="email"
          placeholder="Email"
          value={formData.email}
          onChange={handleChange}
        />

        <input
          type="text"
          name="phone_number"
          placeholder="Phone Number"
          value={formData.phone_number}
          onChange={handleChange}
        />

        <button
          onClick={createCustomer}
          style={{
            background: "blue",
            color: "white",
            border: "none",
            padding: "10px 20px",
            borderRadius: "5px"
          }}
        >
          Create Customer
        </button>

      </div>

      <table border="1">

        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Email</th>
            <th>Phone Number</th>
          </tr>
        </thead>

        <tbody>

          {customers.map(customer => (

            <tr key={customer.id}>
              <td>{customer.id}</td>
              <td>{customer.full_name}</td>
              <td>{customer.email}</td>
              <td>{customer.phone_number}</td>
            </tr>

          ))}

        </tbody>

      </table>

    </div>
  );
}

export default Customers;
