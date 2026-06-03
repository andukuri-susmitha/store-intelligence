# Engineering Choices and Trade-offs

## Choice 1: YOLOv8m for Person Detection

Options Considered:

* YOLOv8n
* YOLOv8m
* YOLOv11
* Faster R-CNN

Decision:

YOLOv8m

Reasoning:

YOLOv8m provides a good balance between:

* Detection accuracy
* Processing speed
* Ease of deployment

Trade-off:

Higher compute cost than YOLOv8n but better detection quality.

---

## Choice 2: ByteTrack for Tracking

Options Considered:

* SORT
* DeepSORT
* ByteTrack

Decision:

ByteTrack

Reasoning:

ByteTrack performs well in crowded environments and retains identities even when detections temporarily disappear.

Trade-off:

Slightly higher complexity than SORT but improved tracking quality.

---

## Choice 3: Event-Based Architecture

Decision:

Generate structured visitor events before computing metrics.

Reasoning:

Separating detection from analytics improves maintainability.

Benefits:

* Easier debugging
* Reusable analytics layer
* Clear audit trail

Trade-off:

Additional storage requirement.

---

## Choice 4: JSON Storage

Decision:

Store events in events.json.

Reasoning:

Fast implementation suitable for challenge timelines.

Trade-off:

Not suitable for large-scale production workloads.

Production Alternative:

PostgreSQL or Kafka.

---

## Choice 5: FastAPI

Decision:

FastAPI selected for serving analytics.

Reasoning:

* Lightweight
* Fast
* Automatic API documentation
* Easy deployment

Trade-off:

Requires separate dashboard application.

---

## Choice 6: Funnel Estimation

Decision:

Estimate intermediate funnel stages from visitor counts.

Reasoning:

The provided CCTV footage does not explicitly contain zone-level labels.

Trade-off:

Approximation rather than exact behavioral tracking.

Production Alternative:

Zone polygons and event transitions.

---

## Choice 7: Conversion Logic

Decision:

Use transaction records as completed purchases.

Formula:

Conversion Rate = Transactions / Unique Visitors × 100

Reasoning:

This directly aligns with retail business objectives.

Trade-off:

Visitor-to-purchase attribution is not available in the provided dataset.

---

## Choice 8: Real-Time vs Batch Processing

Decision:

Batch processing.

Reasoning:

Challenge dataset consists of recorded CCTV footage.

Trade-off:

Not real-time.

Production Alternative:

RTSP camera streams with Kafka event ingestion.

---

## Choice 9: Anomaly Detection

Decision:

Rule-based anomaly detection.

Reasoning:

Simple, explainable, and reliable.

Examples:

* Conversion < 20%
* Conversion > 80%

Trade-off:

Less sophisticated than ML-based anomaly detection.

---

# Future Improvements

* Zone-based customer journey tracking
* Cross-camera re-identification
* Real-time Kafka streaming
* PostgreSQL event storage
* ML-based anomaly detection
* Multi-store analytics aggregation

These enhancements would move the system closer to a production-grade retail intelligence platform.
