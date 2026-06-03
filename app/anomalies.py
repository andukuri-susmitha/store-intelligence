from metrics import get_metrics

def get_anomalies():

    m = get_metrics()

    anomalies = []

    if m["conversion_rate"] < 20:
        anomalies.append(
            "LOW_CONVERSION"
        )

    if m["conversion_rate"] > 80:
        anomalies.append(
            "UNUSUALLY_HIGH_CONVERSION"
        )

    return {
        "anomalies": anomalies
    }