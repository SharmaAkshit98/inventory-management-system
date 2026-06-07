import axios from "axios";

const api = axios.create({
  baseURL: "https://inventory-backend-9pix.onrender.com"
});

export default api;
