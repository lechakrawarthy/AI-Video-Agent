export default function InputForm({onSubmit}){
const data = {
topic:"AI in Education",
description:"AI improving student learning",
duration:15,
tone:"informative",
voice_type:"female",
language:"English"
};


return <button onClick={()=>onSubmit(data)}>Generate Video</button>;
}