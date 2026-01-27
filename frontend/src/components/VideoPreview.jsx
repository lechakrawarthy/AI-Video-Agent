export default function VideoPreview({video}){
return video ? <video src={video} controls width="320"/> : null;
}