from ultralytics import YOLO
import supervision as sv
import cv2
import json
import os
from datetime import datetime

model = YOLO("yolov8m.pt")
tracker = sv.ByteTrack()

VIDEOS = [
    "data/CAM 1.mp4",
    "data/CAM 2.mp4",
    "data/CAM 3.mp4",
    "data/CAM 4.mp4",
    "data/CAM 5.mp4"
]

events = []

for video_path in VIDEOS:

    print("\n--------------------------------")
    print("Processing:", video_path)

    if not os.path.exists(video_path):
        print("File not found!")
        continue

    camera = os.path.basename(video_path)

    cap = cv2.VideoCapture(video_path)

    print("Opened:", cap.isOpened())

    if not cap.isOpened():
        continue

    frame_count = 0

    while True:

        ret, frame = cap.read()

        if not ret:
            print("End of video")
            break

        frame_count += 1

        # Process every 10th frame only
        if frame_count % 100 != 0:
            continue

        results = model(
            frame,
            imgsz=1280,
            conf=0.25,
            verbose=False
        )[0]

        print(
            f"Frame {frame_count} | Detections:",
            len(results.boxes)
        )

        detections = sv.Detections.from_ultralytics(
            results
        )

        if len(detections) == 0:
            continue

        detections = detections[
            detections.class_id == 0
        ]

        print(
            "Person detections:",
            len(detections)
        )

        if len(detections) == 0:
            continue

        detections = tracker.update_with_detections(
            detections
        )

        if detections.tracker_id is None:
            continue

        for track_id in detections.tracker_id:

            events.append({
                "visitor_id":
                f"{camera}_{int(track_id)}",

                "event_type":
                "ENTRY",

                "camera":
                camera,

                "timestamp":
                str(datetime.now())
            })

    cap.release()

with open(
    "data/events.json",
    "w"
) as f:

    json.dump(
        events,
        f,
        indent=4
    )

print("\n========================")
print("Events generated:", len(events))
print("========================")