
"""
Prompt:
Validate event generation output.
"""

import json

def test_events():

    with open(
        "data/events.json"
    ) as f:

        events = json.load(f)

    assert isinstance(
        events,
        list
    )