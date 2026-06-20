"""
SomnoCare - Machine Learning Training Pipeline

Models:
- Sleep disorder classification
- Sleep quality prediction
- Sleep pattern clustering
"""


# ==============================
# Imports
# ==============================

import os
import pickle
import warnings

import pandas as pd
import numpy as np


from imblearn.over_sampling import SMOTE


from sklearn.model_selection import train_test_split


from sklearn.preprocessing import (
    LabelEncoder,
    StandardScaler
)


from sklearn.linear_model import LogisticRegression


from sklearn.tree import DecisionTreeClassifier


from sklearn.ensemble import (
    RandomForestClassifier,
    RandomForestRegressor
)


from sklearn.cluster import KMeans


from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


warnings.filterwarnings("ignore")



# ==============================
# Load Dataset
# ==============================


DATA_PATH = "data/sleep_health_ai_final_dataset.csv"


df = pd.read_csv(DATA_PATH)


print("\nDataset Loaded")
print("Shape:", df.shape)



# ==============================
# Preprocessing
# ==============================


df["Sleep Disorder"] = (
    df["Sleep Disorder"]
    .fillna("None")
)



X = df.drop(
    [
        "Sleep Disorder",
        "Quality of Sleep"
    ],
    axis=1
)



y_disorder = df["Sleep Disorder"]


y_quality = df["Quality of Sleep"]



label_encoders = {}



categorical_columns = (
    X.select_dtypes(
        include=["object"]
    )
    .columns
)



for column in categorical_columns:


    encoder = LabelEncoder()


    X[column] = (
        encoder.fit_transform(
            X[column]
        )
    )


    label_encoders[column] = encoder




target_encoder = LabelEncoder()


y_disorder_encoded = (
    target_encoder.fit_transform(
        y_disorder
    )
)



scaler = StandardScaler()


X_scaled = scaler.fit_transform(
    X
)



print("Preprocessing Completed")



# ==============================
# Disorder Classification
# ==============================


smote = SMOTE(
    random_state=42
)



X_resampled, y_resampled = (
    smote.fit_resample(
        X_scaled,
        y_disorder_encoded
    )
)



X_train, X_test, y_train, y_test = (
    train_test_split(
        X_resampled,
        y_resampled,
        test_size=0.2,
        random_state=42,
        stratify=y_resampled
    )
)



classification_models = {


    "Logistic Regression":

        LogisticRegression(
            max_iter=1000
        ),


    "Decision Tree":

        DecisionTreeClassifier(
            random_state=42
        ),


    "Random Forest":

        RandomForestClassifier(
            n_estimators=500,
            max_depth=25,
            min_samples_split=3,
            random_state=42,
            n_jobs=-1
        )

}



model_results = {}



for name, model in classification_models.items():


    model.fit(
        X_train,
        y_train
    )


    prediction = model.predict(
        X_test
    )


    model_results[name] = (
        accuracy_score(
            y_test,
            prediction
        )
    )




print("\nClassification Results:")



for name, score in model_results.items():


    print(
        f"{name}: {score:.3f}"
    )



best_model_name = max(
    model_results,
    key=model_results.get
)



disorder_model = (
    classification_models[
        best_model_name
    ]
)



final_prediction = (
    disorder_model.predict(
        X_test
    )
)



print(
    "\nSelected Model:",
    best_model_name
)



print(
    classification_report(
        y_test,
        final_prediction,
        target_names=target_encoder.classes_
    )
)



print("\nConfusion Matrix:")


print(
    confusion_matrix(
        y_test,
        final_prediction
    )
)



# Feature importance

if hasattr(
    disorder_model,
    "feature_importances_"
):


    feature_importance = pd.DataFrame(

        {

            "Feature":
                X.columns,


            "Importance":
                disorder_model.feature_importances_

        }

    )



    feature_importance = (

        feature_importance.sort_values(

            by="Importance",

            ascending=False

        )

    )



    print("\nTop Important Features:")


    print(
        feature_importance.head(10)
    )



    # ==============================
# Sleep Quality Prediction
# ==============================


X_train_q, X_test_q, y_train_q, y_test_q = (
    train_test_split(
        X_scaled,
        y_quality,
        test_size=0.2,
        random_state=42
    )
)



quality_model = RandomForestRegressor(
    n_estimators=400,
    max_depth=20,
    random_state=42,
    n_jobs=-1
)



quality_model.fit(
    X_train_q,
    y_train_q
)



quality_prediction = (
    quality_model.predict(
        X_test_q
    )
)



mae = mean_absolute_error(
    y_test_q,
    quality_prediction
)



rmse = np.sqrt(
    mean_squared_error(
        y_test_q,
        quality_prediction
    )
)



r2 = r2_score(
    y_test_q,
    quality_prediction
)



print("\nSleep Quality Model:")


print(
    f"MAE: {mae:.2f}"
)


print(
    f"RMSE: {rmse:.2f}"
)


print(
    f"R2 Score: {r2:.2f}"
)




# ==============================
# Sleep Pattern Clustering
# ==============================


sleep_twin_model = KMeans(
    n_clusters=4,
    random_state=42,
    n_init=10
)



clusters = (
    sleep_twin_model.fit_predict(
        X_scaled
    )
)



df["Sleep Cluster"] = clusters



cluster_summary = (

    df.groupby(
        "Sleep Cluster"
    )
    [
        [
            "Sleep Duration",
            "Stress Level",
            "Quality of Sleep",
            "Physical Activity Level",
            "Screen Time Before Bed"
        ]
    ]
    .mean()

)



print("\nSleep Cluster Summary:")


print(
    cluster_summary
)




# ==============================
# Save Training Artifacts
# ==============================


os.makedirs(
    "models",
    exist_ok=True
)



model_files = {


    "models/disorder_model.pkl":

        disorder_model,



    "models/quality_model.pkl":

        quality_model,



    "models/sleep_twin_model.pkl":

        sleep_twin_model,



    "models/scaler.pkl":

        scaler,



    "models/label_encoders.pkl":

        label_encoders,



    "models/target_encoder.pkl":

        target_encoder,



    "models/feature_columns.pkl":

        X.columns.tolist()

}




for filepath, model_object in model_files.items():


    with open(
        filepath,
        "wb"
    ) as file:


        pickle.dump(
            model_object,
            file
        )




print(
    "\nTraining completed. Model files generated successfully."
)