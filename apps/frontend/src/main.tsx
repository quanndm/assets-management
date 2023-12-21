import React from "react";
import ReactDOM from "react-dom/client";
import "./common/styles/index.scss";
import Router from "./routes/root.tsx";
import "react-toastify/dist/ReactToastify.css";
import ToastWrapper from "./components/Toast/ToastContainer.tsx";

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <Router />
    <ToastWrapper />
  </React.StrictMode>,
);
