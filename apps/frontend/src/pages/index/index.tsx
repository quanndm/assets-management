import { toast } from "react-toastify";
function Home() {
  const showToast = () => {
    toast.success("🦄 Wow so easy!", {});
  };

  return (
    <>
      <button
        onClick={showToast}
        className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full"
      >
        Notify !
      </button>
    </>
  );
}

export default Home;
