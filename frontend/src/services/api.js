export async function generateVideo(data){
const res = await fetch("http://localhost:8000/generate-video",{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify(data)
});
return res.json();
}