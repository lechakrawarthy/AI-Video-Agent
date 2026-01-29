#!/bin/bash

echo "🚀 Starting AI Video Generator..."
echo ""

# Start Backend
echo "📦 Starting Backend Server..."
cd backend
python -m uvicorn app.main:app --reload &
BACKEND_PID=$!

cd ..

# Wait a bit for backend to start
sleep 2

# Start Frontend
echo "🎨 Starting Frontend Dev Server..."
cd frontend
npm run dev &
FRONTEND_PID=$!

cd ..

echo ""
echo "✅ Servers Started!"
echo ""
echo "Backend:  http://127.0.0.1:8000"
echo "Frontend: http://localhost:5173"
echo ""
echo "Press Ctrl+C to stop both servers."

# Wait for Ctrl+C
trap "kill $BACKEND_PID $FRONTEND_PID; exit" INT
wait
