type Props = {
    videoUrl: string;
};

export default function VideoPreview({ videoUrl }: Props) {
    return (
        <div className="max-w-4xl mx-auto mt-8 bg-slate-900 rounded-2xl p-8">
            <h3 className="text-xl font-bold text-white mb-4">Video Preview</h3>
            <video
                src={videoUrl}
                controls
                className="w-full rounded-lg shadow-xl"
            />
        </div>
    );
}
