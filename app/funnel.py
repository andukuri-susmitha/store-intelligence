from metrics import get_metrics

def get_funnel():

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