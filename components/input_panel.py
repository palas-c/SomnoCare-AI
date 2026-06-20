"""
Sleep health input form component for SomnoCare AI.
"""

import streamlit as st


def get_user_inputs():
    """Collect user sleep, health, and lifestyle information."""

    st.markdown(
        """
        <div class="dashboard-card">

        <h2>🌙 Sleep Profile</h2>
        <p>Complete sleep health analysis form</p>

        </div>
        """,
        unsafe_allow_html=True
    )


    tab1, tab2, tab3 = st.tabs(
        [
            "👤 Basic",
            "🧠 Health",
            "🌎 Lifestyle"
        ]
    )


    # Basic information
    with tab1:

        col1, col2 = st.columns(2)

        with col1:

            gender = st.selectbox(
                "Gender",
                ["Male", "Female"]
            )

            age = st.number_input(
                "Age",
                10,
                100,
                25
            )

            occupation = st.selectbox(
                "Occupation",
                [
                    "Software Engineer",
                    "Doctor",
                    "Teacher",
                    "Engineer",
                    "Student",
                    "Nurse",
                    "Manager",
                    "Sales Representative",
                    "Accountant"
                ]
            )

            sleep_duration = st.slider(
                "Sleep Duration",
                0.0,
                12.0,
                7.0
            )


        with col2:

            sleep_efficiency = st.slider(
                "Sleep Efficiency",
                0,
                100,
                85
            )

            sleep_consistency = st.slider(
                "Sleep Consistency",
                0,
                100,
                80
            )

            deep_sleep = st.slider(
                "Deep Sleep Percentage",
                0,
                100,
                25
            )

            rem_sleep = st.slider(
                "REM Sleep Percentage",
                0,
                100,
                25
            )


    # Health information
    with tab2:

        col1, col2 = st.columns(2)

        with col1:

            stress = st.slider(
                "Stress Level",
                1,
                10,
                5
            )

            anxiety = st.slider(
                "Anxiety Level",
                1,
                10,
                5
            )

            mood = st.slider(
                "Mood Score",
                1,
                10,
                7
            )

            fatigue = st.slider(
                "Fatigue Level",
                1,
                10,
                5
            )

            bmi = st.number_input(
                "BMI",
                value=22.0
            )

            bmi_category = st.selectbox(
                "BMI Category",
                [
                    "Normal",
                    "Overweight",
                    "Obese"
                ]
            )


        with col2:

            blood_pressure = st.text_input(
                "Blood Pressure",
                "120/80"
            )

            heart_rate = st.number_input(
                "Heart Rate",
                value=70
            )

            resting_hr = st.number_input(
                "Resting Heart Rate",
                value=65
            )

            night_awake = st.number_input(
                "Night Awakenings",
                value=1
            )


    # Lifestyle information
    with tab3:

        col1, col2 = st.columns(2)

        with col1:

            activity = st.slider(
                "Physical Activity Level",
                0,
                100,
                50
            )

            exercise = st.slider(
                "Exercise Frequency",
                0,
                7,
                3
            )

            steps = st.number_input(
                "Daily Steps",
                value=5000
            )

            calories = st.number_input(
                "Calories Burned",
                value=2200
            )

            screen = st.slider(
                "Screen Time Before Bed",
                0.0,
                10.0,
                2.0
            )


        with col2:

            caffeine = st.slider(
                "Caffeine Intake",
                0,
                10,
                2
            )

            alcohol = st.selectbox(
                "Alcohol Consumption",
                [
                    "No",
                    "Occasionally",
                    "Regular"
                ]
            )

            smoking = st.selectbox(
                "Smoking Status",
                [
                    "Never",
                    "Former",
                    "Current"
                ]
            )

            work = st.slider(
                "Work Hours",
                0,
                16,
                8
            )

            noise = st.selectbox(
                "Noise Level",
                [
                    "Low",
                    "Medium",
                    "High"
                ]
            )

            temperature = st.slider(
                "Room Temperature",
                10,
                35,
                22
            )

            light = st.selectbox(
                "Light Exposure Before Sleep",
                [
                    "Low",
                    "Medium",
                    "High"
                ]
            )


    # Model input dictionary
    return {
        "Gender": gender,
        "Age": age,
        "Occupation": occupation,

        "Sleep Duration": sleep_duration,
        "Sleep Efficiency": sleep_efficiency,
        "Sleep Consistency": sleep_consistency,
        "Deep Sleep Percentage": deep_sleep,
        "REM Sleep Percentage": rem_sleep,

        "Physical Activity Level": activity,
        "Stress Level": stress,

        "BMI Category": bmi_category,
        "BMI": bmi,

        "Blood Pressure": blood_pressure,
        "Heart Rate": heart_rate,
        "Resting Heart Rate": resting_hr,

        "Daily Steps": steps,

        "Night Awakenings": night_awake,
        "Exercise Frequency": exercise,
        "Calories Burned": calories,

        "Screen Time Before Bed": screen,
        "Caffeine Intake": caffeine,
        "Alcohol Consumption": alcohol,
        "Smoking Status": smoking,

        "Work Hours": work,

        "Anxiety Level": anxiety,
        "Mood Score": mood,
        "Fatigue Level": fatigue,

        "Noise Level": noise,
        "Room Temperature": temperature,
        "Light Exposure Before Sleep": light
    }