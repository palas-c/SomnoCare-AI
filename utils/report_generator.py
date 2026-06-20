"""
PDF report generator for SomnoCare AI.

Creates downloadable sleep analysis reports.
"""

import os

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


REPORT_PATH = "reports/SomnoCare_Report.pdf"


def generate_report(record):
    """Generate a PDF report from sleep analysis data."""

    os.makedirs(
        "reports",
        exist_ok=True
    )


    document = SimpleDocTemplate(
        REPORT_PATH
    )


    styles = getSampleStyleSheet()

    content = []


    content.append(
        Paragraph(
            "SomnoCare AI Sleep Report",
            styles["Title"]
        )
    )


    content.append(
        Spacer(
            1,
            20
        )
    )


    content.append(
        Paragraph(
            f"Generated: {record['timestamp']}",
            styles["Normal"]
        )
    )


    prediction = record["prediction"]


    content.append(
        Paragraph(
            "Sleep Analysis Results",
            styles["Heading2"]
        )
    )


    content.append(
        Paragraph(
            f"""
            Sleep Disorder:
            {prediction["sleep_disorder"]}
            <br/>

            Sleep Quality:
            {prediction["sleep_quality"]}
            <br/>

            Sleep Profile:
            {prediction["sleep_profile"]}
            """,
            styles["Normal"]
        )
    )


    insights = record["insights"]


    content.append(
        Paragraph(
            "Sleep Insights",
            styles["Heading2"]
        )
    )


    content.append(
        Paragraph(
            insights["summary"],
            styles["Normal"]
        )
    )


    content.append(
        Paragraph(
            "Recommendations",
            styles["Heading2"]
        )
    )


    for recommendation in insights["recommendations"]:

        content.append(
            Paragraph(
                f"- {recommendation}",
                styles["Normal"]
            )
        )


    document.build(
        content
    )


    return REPORT_PATH