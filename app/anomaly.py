def detect_anomalies(metrics):

    anomalies = []

    if metrics[
        "conversion_rate"
    ] < 5:

        anomalies.append(
            "LOW_CONVERSION"
        )

    if metrics[
        "unique_visitors"
    ] > 1000:

        anomalies.append(
            "FOOTFALL_SPIKE"
        )

    return anomalies