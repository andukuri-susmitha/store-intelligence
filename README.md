# Store Intelligence System

## Run Detection

python app/multi_camera_processor.py

## Run API

python -m uvicorn app.api:app --reload

API Docs:

http://127.0.0.1:8000/docs

## Run Dashboard

python -m streamlit run app/dashboard.py

Dashboard URL:

http://localhost:8501

## Docker

docker compose up

## Dataset

The CCTV video files are not included in this repository as per challenge instructions.

Place the following files inside the data/ directory before running the pipeline:

- CAM 1.mp4
- CAM 2.mp4
- CAM 3.mp4
- CAM 4.mp4
- CAM 5.mp4