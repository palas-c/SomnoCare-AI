"""
Generates personalized sleep insights based on
prediction results and user lifestyle data.
"""


def generate_sleep_insights(prediction, user_data):
    """Create sleep health summary and recommendations."""

    insights = []
    recommendations = []


    disorder = prediction["sleep_disorder"]
    quality = prediction["sleep_quality"]
    profile = prediction["sleep_profile"]


    # Sleep quality analysis
    if quality >= 8:

        insights.append(
            "Your sleep quality score indicates a healthy sleep pattern."
        )


    elif quality >= 6:

        insights.append(
            "Your sleep quality is moderate and may improve with lifestyle adjustments."
        )


    else:

        insights.append(
            "Your sleep quality score suggests that improvement may be beneficial."
        )


    # Disorder prediction explanation
    if disorder != "None":

        insights.append(
            f"Your sleep pattern shows similarities with {disorder} patterns."
        )


    else:

        insights.append(
            "No major sleep disorder pattern was detected from the provided data."
        )


    # Stress analysis
    if user_data.get("Stress Level", 0) >= 7:

        recommendations.append(
            "Practice relaxation techniques to reduce stress before bedtime."
        )


    # Screen usage
    if user_data.get("Screen Time Before Bed", 0) > 2:

        recommendations.append(
            "Reduce screen exposure before sleep to support better rest."
        )


    # Physical activity analysis
    if user_data.get("Exercise Frequency", 0) < 3:

        recommendations.append(
            "Increase weekly physical activity to improve sleep consistency."
        )


    # Sleep duration analysis
    if user_data.get("Sleep Duration", 8) < 7:

        recommendations.append(
            "Try maintaining 7-9 hours of consistent sleep."
        )


    if len(recommendations) == 0:

        recommendations.append(
            "Maintain your current sleep habits and routine."
        )


    return {
        "summary": " ".join(insights),
        "sleep_profile": profile,
        "recommendations": recommendations
    }