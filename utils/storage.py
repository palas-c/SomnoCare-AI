"""
Local history storage system for SomnoCare AI.

Stores and retrieves sleep analysis records.
"""

import json
import os

from datetime import datetime


STORAGE_PATH = "data/history.json"


def save_analysis(user_data, prediction, insights):
    """Save a sleep analysis record."""

    record = {
        "timestamp": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),

        "user_data": user_data,
        "prediction": prediction,
        "insights": insights
    }


    os.makedirs(
        "data",
        exist_ok=True
    )


    history = load_history()

    history.append(record)


    with open(
        STORAGE_PATH,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            history,
            file,
            indent=4
        )


def load_history():
    """Load saved analysis history."""

    if not os.path.exists(STORAGE_PATH):
        return []


    try:

        with open(
            STORAGE_PATH,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)


    except json.JSONDecodeError:

        return []


def clear_history():
    """Remove all saved analysis records."""

    if os.path.exists(STORAGE_PATH):

        os.remove(STORAGE_PATH)