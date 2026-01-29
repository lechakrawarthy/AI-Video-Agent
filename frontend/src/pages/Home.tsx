import { useState } from "react";
import { generateVideo } from "../api";
import InputForm from "../components/InputForm";
import VideoResult from "../components/VideoResult";
import Loader from "../components/Loader";

export default function Home() {
  const [result, setResult] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  async function handleSubmit(data: any) {
    setLoading(true);
    setResult(null);

    const res = await generateVideo(data);
    setResult(res);

    setLoading(false);
  }

  return (
    <div className="min-h-screen bg-slate-950 text-white">
      {/* Header */}
      <div className="flex items-center justify-between px-10 py-6 border-b border-slate-800">
        <div className="text-xl font-bold">⚡ ShortsVibe AI</div>
        <div className="space-x-6 text-slate-300">
          <span className="cursor-pointer hover:text-white">Home</span>
          <span className="cursor-pointer hover:text-white">My Projects</span>
          <span className="cursor-pointer hover:text-white">Resources</span>
          <button className="ml-4 px-4 py-2 rounded-lg bg-slate-800">
            Sign In
          </button>
        </div>
      </div>

      {/* Form */}
      <div className="py-12">
        <InputForm onSubmit={handleSubmit} />

        {loading && <Loader />}

        {result && <VideoResult data={result} />}
      </div>
    </div>
  );
}
