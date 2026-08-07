"""
FastAPI application entry point.

Endpoints:
    POST /analyze      — Analyze uploaded drone image (YOLO placeholder)
    POST /predict      — Predict yield from field data
    GET  /weather      — Current weather conditions
    GET  /missions     — Mission history records
    GET  /dashboard    — Aggregated dashboard statistics
    GET  /spray-zones  — Precision spray zone recommendations
    GET  /heatmap      — Field heatmap grid data
    GET  /             — Health check
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import analyze, predict, weather, missions, dashboard, spray, heatmap

app = FastAPI(
    title="Indigenous Edge AI Drone Platform",
    description="Precision Agriculture AI — Backend API for drone imagery analysis, "
                "yield prediction, and mission management.",
    version="1.0.0",
)

# CORS — allow the Vite dev server and any frontend origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def health_check():
    return {
        "status": "online",
        "service": "AgriEdge AI Backend",
        "version": "1.0.0",
        "ai_engine": "YOLOv8-Agri v2.3.1 (mock)",
    }


# Register routers
app.include_router(analyze.router)
app.include_router(predict.router)
app.include_router(weather.router)
app.include_router(missions.router)
app.include_router(dashboard.router)
app.include_router(spray.router)
app.include_router(heatmap.router)
