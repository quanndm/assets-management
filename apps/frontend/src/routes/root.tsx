import { createBrowserRouter, RouterProvider } from "react-router-dom";
import Home from "../pages/index";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Home />,
  },
]);

export default function Root() {
  return <RouterProvider router={router} />;
}
