# Indigenous Edge AI Drone Platform — Backend

FastAPI backend for the Precision Agriculture AI drone platform.

## Quick Start

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

The API will be available at `http://localhost:8000`.

Interactive API docs: `http://localhost:8000/docs`

## Endpoints

| Method | Path            | Description                          |
|--------|-----------------|--------------------------------------|
| GET    | `/`             | Health check                         |
| POST   | `/analyze`      | Analyze drone image (YOLO placeholder) |
| POST   | `/predict`      | Predict crop yield                   |
| GET    | `/weather`      | Current weather conditions           |
| GET    | `/missions`     | Mission history records              |
| GET    | `/dashboard`    | Aggregated dashboard statistics      |
| GET    | `/spray-zones`  | Spray zone recommendations           |
| GET    | `/heatmap`      | Field heatmap grid data              |

## YOLO Integration

The detection service is in `app/services/detector.py`. It currently
returns mock data. To integrate a real YOLOv8 model:

```python
# app/services/detector.py
from ultralytics import YOLO

class CropDetector:
    def __init__(self):
        self.model = YOLO("yolov8-agri.pt")

    def detect(self, image_bytes):
        results = self.model(image_bytes)
        return self._parse(results)
```

No router or frontend changes needed — the API contract stays the same.

## Architecture

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI app entry point
│   ├── routers/             # API route handlers
│   │   ├── __init__.py
│   │   ├── analyze.py        # POST /analyze
│   │   ├── predict.py       # POST /predict
│   │   ├── weather.py       # GET /weather
│   │   ├── missions.py      # GET /missions
│   │   ├── dashboard.py     # GET /dashboard
│   │   ├── spray.py         # GET /spray-zones
│   │   └── heatmap.py       # GET /heatmap
│   ├── services/
│   │   ├── __init__.py
│   │   └── detector.py      # YOLO detection (mock placeholder)
│   └── data/
│       ├── __init__.py
│       └── mock_data.py      # Mock JSON data
└── requirements.txt
```
