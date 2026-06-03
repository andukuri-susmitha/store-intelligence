# Store Intelligence System – Design Document

## Problem Statement

The objective is to build an end-to-end Store Intelligence System that converts raw CCTV footage into business metrics such as visitor count, conversion rate, funnel analytics, and anomaly detection.

The system processes multiple CCTV streams, detects and tracks visitors, generates structured events, and exposes analytics through production-style APIs.

---

# System Architecture

## Input Layer

Sources:

* CAM 1.mp4
* CAM 2.mp4
* CAM 3.mp4
* CAM 4.mp4
* CAM 5.mp4

These CCTV feeds act as raw input for the intelligence pipeline.

---

## Detection Layer

Model:
YOLOv8m

Responsibilities:

* Detect persons in each frame
* Ignore non-human objects
* Generate bounding boxes
* Filter low-confidence detections

Output:

Person detections with coordinates and confidence scores.

---

## Tracking Layer

Tracker:
ByteTrack

Responsibilities:

* Assign unique IDs to detected visitors
* Maintain identity across frames
* Reduce duplicate counting
* Handle short occlusions

Output:

Tracked visitor IDs.

Example:

Visitor #12 remains Visitor #12 while moving through the scene.

---

## Event Generation Layer

Tracked visitors are converted into business events.

Event Schema:

{
"visitor_id": "CAM1_12",
"event_type": "ENTRY",
"camera": "CAM1",
"timestamp": "2026-06-01T10:15:00"
}

Events are stored in events.json.

---

## Analytics Layer

Analytics are computed using:

1. Visitor Events
2. Store Transaction Data

Generated Metrics:

* Unique Visitors
* Transactions
* Conversion Rate

Formula:

Conversion Rate = Transactions / Unique Visitors × 100

---

## Funnel Analytics

Visitor journey is represented as:

Entered Store
↓
Zone Visit
↓
Billing Area
↓
Purchase

This allows measurement of drop-off between stages.

---

## Anomaly Detection

The system detects:

* Low conversion rate
* Unusually high conversion rate
* Sudden visitor spikes

These anomalies are exposed through APIs.

---

## API Layer

FastAPI exposes:

GET /health

Returns system status.

GET /metrics

Returns:

{
"unique_visitors": 43,
"transactions": 24,
"conversion_rate": 55.81
}

GET /funnel

Returns funnel stage counts.

GET /anomalies

Returns detected anomalies.

---

## Dashboard Layer

Streamlit dashboard provides:

* Visitor count
* Conversion rate
* Funnel visualization
* Anomaly summary

This enables business users to consume insights without interacting with raw events.

---

# Scalability Considerations

For production deployment:

* Kafka can replace local event files.
* PostgreSQL can replace JSON storage.
* Redis can be used for caching metrics.
* Kubernetes can be used for scaling inference services.

---

# Observability

Logs:

* Video processing status
* Detection counts
* Event generation counts

Metrics:

* Total visitors
* Total transactions
* Conversion rate

---

# AI-Assisted Decisions

AI assistance was used for:

* Evaluating detection models
* Comparing tracking approaches
* Designing event schemas
* Generating API structure
* Exploring production deployment strategies

Final architectural decisions, implementation, and trade-offs were independently reviewed and selected based on challenge requirements.

---

# Limitations

Current implementation assumes:

* Single-store environment
* Limited camera overlap
* Simplified funnel estimation
* Local JSON-based event storage

These trade-offs were made to prioritize end-to-end system functionality within challenge constraints.
