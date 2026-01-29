export default function VideoResult({ data }: any) {
  if (!data) return null;

  return (
    <div className="max-w-4xl mx-auto mt-8 bg-slate-900 rounded-2xl p-8 text-white">
      <h2 className="text-2xl font-bold mb-6 text-purple-400">✨ Video Generated!</h2>

      {data.video_url && (
        <div className="mb-8">
          <h3 className="text-xl font-semibold mb-3">Final Video</h3>
          <video
            className="w-full rounded-lg shadow-xl"
            controls
            src={`http://localhost:8000/${data.video_url}`}
          >
            Your browser does not support the video tag.
          </video>
        </div>
      )}

      {data.scenes && (
        <div className="mt-6">
          <h3 className="text-xl font-semibold mb-3">Scene Breakdown</h3>
          <div className="space-y-3">
            {data.scenes.map((scene: any, i: number) => (
              <div key={i} className="bg-slate-800 p-4 rounded-lg">
                <div className="text-purple-300 font-semibold">Scene {scene.scene}</div>
                <div className="text-slate-300 mt-1">{scene.text}</div>
                <div className="text-slate-500 text-sm mt-1">{scene.duration}s</div>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
