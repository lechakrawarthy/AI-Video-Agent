import { useState } from "react";
import { generateVideo } from "../api";
import InputForm from "../components/InputForm";
import VideoResult from "../components/VideoResult";

export default function Home() {
  const [result, setResult] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  async function handleSubmit(data: any) {
    setLoading(true);
    setResult(null);

    try {
      const res = await generateVideo(data);
      setResult(res);
    } catch (error) {
      console.error("Error generating video:", error);
      alert("Failed to generate video");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div style={{ padding: "20px" }}>
      <h1>AI Video Generator</h1>

      {/* Input form */}
      <InputForm onSubmit={handleSubmit} />

      {/* Loading state */}
      {loading && <p>Generating video... Please wait.</p>}

      {/* Result */}
      {result && <VideoResult data={result} />}
    </div>
  );
}
