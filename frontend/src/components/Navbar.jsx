import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav
      style={{
        background: "#1f2937",
        padding: "15px",
        display: "flex",
        gap: "20px"
      }}
    >
      <Link to="/">Dashboard</Link>

      <Link to="/products">Products</Link>

      <Link to="/customers">Customers</Link>

      <Link to="/orders">Orders</Link>
    </nav>
  );
}

export default Navbar;
