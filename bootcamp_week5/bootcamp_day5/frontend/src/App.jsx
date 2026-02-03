import { useEffect, useState } from "react";

function App() {
  const [msg, setMsg] = useState("Loading...");

  useEffect(() => {
    fetch(import.meta.env.VITE_SERVER_URL)
      .then(res => res.json())
      .then(data => setMsg(data.message))
      .catch(() => setMsg("Error contacting server"));
  }, []);

  return (
    <h1>Client → {msg}</h1>
  );
}

export default App;
