"""
Model loading utilities for SomnoCare AI.

Loads trained machine learning models and preprocessing artifacts.
"""

import os
import pickle

import streamlit as st


MODEL_DIR = "models"


@st.cache_resource
def load_pickle_file(filename):
    """Load a pickle artifact from the models directory."""

    file_path = os.path.join(
        MODEL_DIR,
        filename
    )

    with open(
        file_path,
        "rb"
    ) as file:

        return pickle.load(
            file
        )


@st.cache_resource
def load_all_models():
    """Load all ML models and preprocessing artifacts."""

    artifacts = {
        "disorder_model": load_pickle_file(
            "disorder_model.pkl"
        ),

        "quality_model": load_pickle_file(
            "quality_model.pkl"
        ),

        "sleep_twin_model": load_pickle_file(
            "sleep_twin_model.pkl"
        ),

        "scaler": load_pickle_file(
            "scaler.pkl"
        ),

        "label_encoders": load_pickle_file(
            "label_encoders.pkl"
        ),

        "target_encoder": load_pickle_file(
            "target_encoder.pkl"
        ),

        "feature_columns": load_pickle_file(
            "feature_columns.pkl"
        )
    }

    return artifacts