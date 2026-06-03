import json
import pandas as pd

def get_metrics():

    try:
        with open("data/events.json", "r") as f:
            events = json.load(f)
    except:
        events = []

    unique_visitors = len(
        set(
            event["visitor_id"]
            for event in events
        )
    )

    try:
        df = pd.read_csv(
            "data/Brigade_Bangalore_10_April_26 (1)bc6219c.csv"
        )

        transactions = df["invoice_number"].nunique()

    except Exception as e:

        print(e)
        transactions = 0

    conversion_rate = 0

    if unique_visitors > 0:

        conversion_rate = round(
            (transactions / unique_visitors) * 100,
            2
        )

    return {
        "unique_visitors": unique_visitors,
        "transactions": transactions,
        "conversion_rate": conversion_rate
    }