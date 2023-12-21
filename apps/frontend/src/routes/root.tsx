import { createBrowserRouter, RouterProvider } from "react-router-dom";
import Home from "../pages/index";
import { Login } from "../pages/auth";
import React from "react";
import feather from "feather-icons";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Home />,
  },
  {
    path: "auth",
    children: [
      {
        path: "login",
        element: <Login />,
      },
      {
        path: "register",
        element: <div>register</div>,
      },
      {
        path: "forgot-password",
        element: <div>forgot-password</div>,
      },
      {
        path: "reset-password",
        element: <div>reset-password</div>,
      },
    ],
  },
  {
    path: "*", // 404
    element: <div>404</div>,
  },
]);

export default function Root() {
  React.useLayoutEffect(() => {
    feather.replace();
  }, []);

  return <RouterProvider router={router} />;
}
