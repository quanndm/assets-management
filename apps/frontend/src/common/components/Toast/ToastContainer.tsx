import { ToastContainer } from "react-toastify";

const ToastWrapper = () => {
  return (
    <ToastContainer
      autoClose={5000}
      hideProgressBar={false}
      closeOnClick
      pauseOnFocusLoss={false}
      theme="light"
      pauseOnHover={false}
    />
  );
};

export default ToastWrapper;
