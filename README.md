# AI Video / Shorts Generator Agent

An AI-powered application that converts text input into short-form videos using:
- LLM-based script generation
- AI image creation (DALL-E)
- AI voice-over (TTS)
- FFmpeg video assembly

## 🚀 Quick Start

### Prerequisites
- **Python 3.8+**
- **Node.js 16+**
- **FFmpeg** (installed and in PATH)
- **OpenAI API Key** (for AI features)

### 1️⃣ Backend Setup

```bash
cd backend

# Install dependencies
pip install -r requirements.txt

# Configure environment (optional for now)
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY

# Start the server
python -m uvicorn app.main:app --reload
```

Backend will run on: `http://127.0.0.1:8000`

### 2️⃣ Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

Frontend will run on: `http://localhost:5173` (or next available port)

### 3️⃣ Access the Application

Open your browser to the frontend URL (shown in terminal after `npm run dev`)

## 📋 Features

- 📝 Script generation based on topic and description
- 🎨 Scene-by-scene content planning
- 🎤 Voice-over generation
- 🖼️ Image generation for each scene
- 🎬 Automated video assembly
- ⚙️ Customizable tone, voice, and duration

## 🛠️ Tech Stack

### Backend
- **FastAPI** - Modern Python web framework
- **OpenAI API** - GPT for scripts, DALL-E for images, TTS for voice
- **FFmpeg** - Video assembly
- **Pydantic** - Data validation

### Frontend
- **React** - UI framework
- **TypeScript** - Type-safe JavaScript
- **Vite** - Build tool
- **Tailwind CSS** - Styling

## 📁 Project Structure

```
├── backend/
│   ├── app/
│   │   ├── agents/          # AI agent modules
│   │   │   ├── script_agent.py
│   │   │   ├── image_agent.py
│   │   │   ├── voice_agent.py
│   │   │   └── video_agent.py
│   │   ├── main.py          # FastAPI application
│   │   ├── models.py        # Data models
│   │   └── orchestrator.py  # Main workflow
│   ├── outputs/             # Generated files
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/      # React components
│   │   ├── pages/           # Page components
│   │   ├── api.ts           # API client
│   │   └── main.tsx         # Entry point
│   └── package.json
│
└── README.md
```

## 🎯 Use Cases

- 📱 Social media content creation
- 📢 Marketing reels and ads
- 📚 Educational shorts
- 🎥 Quick video prototypes

## 🔧 Troubleshooting

### Backend Issues
- **Port already in use**: Change port with `--port 8001`
- **Module not found**: Run `pip install -r requirements.txt`
- **CORS errors**: Check frontend URL in CORS settings

### Frontend Issues
- **Port in use**: Vite will auto-select next available port
- **Styles not loading**: Ensure dev server is running
- **API errors**: Verify backend is running on port 8000

## 📝 Development Notes

Currently, the application uses placeholder/mock implementations for:
- Image generation (creates empty files)
- Voice generation (creates empty files)
- Video assembly (creates empty file)

To enable full AI features, add your OpenAI API key to `.env` and implement the actual API calls in the agent files.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

MIT License - feel free to use this project for learning or production.
