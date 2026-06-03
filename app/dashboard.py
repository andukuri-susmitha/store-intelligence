
import streamlit as st

from app.metrics import get_metrics

st.title(
    "Store Intelligence Dashboard"
)

m = get_metrics()

st.metric(
    "Visitors",
    m["unique_visitors"]
)

st.metric(
    "Transactions",
    m["transactions"]
)

st.metric(
    "Conversion %",
    m["conversion_rate"]
)

st.write(m)