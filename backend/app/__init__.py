"""
Indigenous Edge AI Drone Platform for Precision Agriculture
FastAPI Backend — Mock Data Implementation

This backend provides REST API endpoints for the agricultural drone
platform. Currently returns mock JSON data. The YOLO/OpenCV integration
is designed as a drop-in replacement — see app/services/detector.py.

Run with:
    uvicorn app.main:app --reload --port 8000

Install with:
    pip install fastapi uvicorn python-multipart pillow
"""

__version__ = "1.0.0"
