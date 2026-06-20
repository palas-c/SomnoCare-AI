"""
Machine learning inference pipeline for SomnoCare AI.

Handles preprocessing and predictions from trained models.
"""

import pandas as pd

from utils.model_loader import load_all_models


# Load trained model artifacts
artifacts = load_all_models()


disorder_model = artifacts["disorder_model"]
quality_model = artifacts["quality_model"]
sleep_twin_model = artifacts["sleep_twin_model"]

scaler = artifacts["scaler"]
label_encoders = artifacts["label_encoders"]
target_encoder = artifacts["target_encoder"]
feature_columns = artifacts["feature_columns"]


SLEEP_PROFILES = {
    0: "Balanced Sleeper",
    1: "High Performance Sleeper",
    2: "Active but Stressed Sleeper",
    3: "Recovery Needed Sleeper"
}


def preprocess_input(user_data):
    """
    Apply the same preprocessing steps
    used during model training.
    """

    input_df = pd.DataFrame([user_data])

    # Match training feature order
    input_df = input_df[feature_columns]


    # Encode categorical features
    for column, encoder in label_encoders.items():

        if column not in input_df.columns:
            continue


        try:
            input_df[column] = encoder.transform(
                input_df[column]
            )


        except ValueError:

            value = input_df[column].values[0]

            raise ValueError(
                f"Invalid value '{value}' for '{column}'. "
                f"Expected: {list(encoder.classes_)}"
            )


    return scaler.transform(input_df)


def predict_sleep_health(user_data):
    """
    Predict sleep disorder, quality score,
    and sleep profile.
    """

    processed_input = preprocess_input(user_data)


    disorder_code = disorder_model.predict(
        processed_input
    )[0]


    disorder = target_encoder.inverse_transform(
        [disorder_code]
    )[0]


    quality_score = quality_model.predict(
        processed_input
    )[0]


    sleep_cluster = sleep_twin_model.predict(
        processed_input
    )[0]


    return {
        "sleep_disorder": disorder,

        "sleep_quality": round(
            float(quality_score),
            2
        ),

        "sleep_profile": SLEEP_PROFILES.get(
            sleep_cluster,
            "Unknown Profile"
        )
    }