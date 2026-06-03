
"""
Prompt:
Validate metrics generation logic.
"""

from app.metrics import get_metrics

def test_metrics():

    m = get_metrics()

    assert "unique_visitors" in m