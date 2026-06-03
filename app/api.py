from fastapi import FastAPI
from app.metrics import get_metrics
from app.anomaly import detect_anomalies

app = FastAPI()


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/metrics")
def metrics():
    return get_metrics()


@app.get("/conversion")
def conversion():
    return get_metrics()


@app.get("/funnel")
def funnel():

    m = get_metrics()

    visitors = m["unique_visitors"]
    transactions = m["transactions"]

    zone_visit = int(visitors * 0.85)
    billing = int(visitors * 0.65)

    if transactions > billing:
        transactions = billing

    return {
        "entered": visitors,
        "zone_visit": zone_visit,
        "billing": billing,
        "purchased": transactions
    }


@app.get("/anomalies")
def anomalies():

    return {
        "anomalies":
        detect_anomalies(
            get_metrics()
        )
    }