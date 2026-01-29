# AI Video Generator - Quick Start Script

Write-Host "🚀 Starting AI Video Generator..." -ForegroundColor Cyan
Write-Host ""

# Check if backend and frontend directories exist
if (-not (Test-Path "backend")) {
    Write-Host "❌ Error: backend directory not found!" -ForegroundColor Red
    exit 1
}

if (-not (Test-Path "frontend")) {
    Write-Host "❌ Error: frontend directory not found!" -ForegroundColor Red
    exit 1
}

# Start Backend
Write-Host "📦 Starting Backend Server..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd backend; python -m uvicorn app.main:app --reload"

Start-Sleep -Seconds 2

# Start Frontend
Write-Host "🎨 Starting Frontend Dev Server..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd frontend; npm run dev"

Start-Sleep -Seconds 3

Write-Host ""
Write-Host "✅ Servers Started!" -ForegroundColor Green
Write-Host ""
Write-Host "Backend:  http://127.0.0.1:8000" -ForegroundColor Cyan
Write-Host "Frontend: http://localhost:5173" -ForegroundColor Cyan
Write-Host ""
Write-Host "Press Ctrl+C in each terminal window to stop the servers." -ForegroundColor Gray
