import { useState } from "react";

export default function InputForm({ onSubmit }: any) {
  const [topic, setTopic] = useState("");
  const [description, setDescription] = useState("");

  function submit() {
    onSubmit({
      topic,
      description,
      duration: 30,
      tone: "informative",
      voice: "male",
      language: "English",
    });
  }

  return (
    <div>
      <input
        placeholder="Video Topic"
        value={topic}
        onChange={(e) => setTopic(e.target.value)}
      />
      <br />
      <textarea
        placeholder="Video Description"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
      />
      <br />
      <button onClick={submit}>Generate Video</button>
    </div>
  );
}
