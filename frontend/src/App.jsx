import {useState} from "react";
import {generateVideo} from "./services/api";


function App(){
const [video,setVideo]=useState(null);


const handleGenerate = async()=>{
const data = await generateVideo({
topic:"AI in Education",
description:"How AI helps students learn",
duration:15,
tone:"informative",
voice_type:"female",
language:"English"
});
setVideo(data.video_url);
}


return(
<div style={{padding:"20px"}}>
<h2>AI Shorts Generator</h2>
<button onClick={handleGenerate}>Generate Video</button>
{video && <video src={video} controls width="320"/>}
</div>
);
}


export default App;