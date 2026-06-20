# SomnoCare AI v2 🌙

SomnoCare AI is a machine learning powered sleep health analysis application that analyzes sleep patterns, predicts possible sleep disorder trends, estimates sleep quality, and provides personalized sleep improvement insights.

The system combines multiple machine learning models with a Streamlit-based interactive dashboard to deliver sleep analysis, AI-generated recommendations, history tracking, and PDF report generation.

---

## Overview

SomnoCare AI focuses on using data-driven techniques to understand sleep behavior.

The application processes user health, lifestyle, and sleep-related inputs through trained ML models and generates meaningful insights through an AI interpretation layer.

---

## Features

### Sleep Health Analysis

- Sleep disorder pattern prediction
- Sleep quality score estimation
- Sleep profile classification
- Lifestyle and health factor analysis

### Doctor AI Insights

- Personalized sleep health summary
- Lifestyle-based recommendations
- Sleep improvement suggestions

### Interactive Dashboard

- Modern Streamlit interface
- User-friendly analysis workflow
- Prediction result dashboard
- Analysis history tracking

### Report Generation

- Automatic PDF report creation
- Downloadable sleep analysis reports

---

## System Architecture

```text
User Input
    |
    v
Streamlit Interface
    |
    v
Prediction Engine
    |
    +----------------------+
    |                      |
    v                      v
ML Models           Doctor AI Engine
    |                      |
    +----------------------+
              |
              v
      Results Dashboard
              |
              v
   History Storage + PDF Reports
```

---

## Machine Learning Pipeline

The project uses multiple machine learning components:

### Sleep Disorder Prediction

A classification model trained to identify possible sleep disorder patterns based on user lifestyle and health parameters.

### Sleep Quality Prediction

A regression model that estimates a user's sleep quality score.

### Sleep Profile Detection

A clustering model that categorizes users into different sleep behavior profiles.

Sleep profiles include:

- Balanced Sleeper
- High Performance Sleeper
- Active but Stressed Sleeper
- Recovery Needed Sleeper

---

## Machine Learning Workflow

```text
Dataset
   |
   v
Data Cleaning
   |
   v
Feature Engineering
   |
   v
Model Training
   |
   v
Model Evaluation
   |
   v
Saved ML Artifacts
   |
   v
Real-Time Prediction System
```

---

## Tech Stack

### Programming Language

- Python

### Machine Learning

- Scikit-learn
- Pandas
- NumPy
- Imbalanced-learn

### Frontend

- Streamlit
- HTML/CSS Styling

### Backend Logic

- Python Modules
- Pickle Model Storage
- JSON Based Local Storage

### Report System

- ReportLab PDF Generation

---

## Project Structure

```text
SomnoCare-AI/

├── app.py

├── assets/
│   └── style.css

├── components/
│   ├── sidebar.py
│   ├── account_panel.py
│   ├── dashboard.py
│   ├── analysis_page.py
│   ├── input_panel.py
│   ├── prediction.py
│   ├── results_page.py
│   ├── doctor_page.py
│   ├── history_page.py
│   └── report_page.py

├── utils/
│   ├── model_loader.py
│   ├── prediction_engine.py
│   ├── doctor_ai.py
│   ├── storage.py
│   └── report_generator.py

├── src/
│   └── train.py

├── notebooks/
│   └── experiments

├── models/
│   └── trained model files

├── data/
│   └── dataset

├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/SomnoCare-AI.git
```

Move into the project directory:

```bash
cd SomnoCare-AI
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## Current Version

SomnoCare AI v2 Core Release:

Completed:

- Machine learning pipeline
- Prediction system
- Streamlit dashboard
- Doctor AI insights
- History management
- PDF reports

---

## Future Improvements

Planned features:

- User authentication system
- Database integration
- User profiles
- Advanced analytics dashboard
- AI sleep coach assistant
- Cloud deployment improvements

---

## Contributors

This project was developed as part of an academic AI/ML project at  
Modern Institute of Engineering and Technology (MIET).

### Project Team

- **Palash Chal** — Machine Learning Engineering, Backend Development, Streamlit Application Development, Model Integration

- **Sayan Ghosh** — Project Research and Documentation

- **Monorama Adhikary** — Research Support and Testing

- **Monisha Maji** — Documentation and Project Analysis


### Project Guide

- **Partha Ghosh** — Faculty Guide, Modern Institute of Engineering and Technology (MIET)

---

## Disclaimer

SomnoCare AI is an educational AI project created for sleep health analysis and research purposes.

The predictions and recommendations generated by this application are not intended to replace professional medical advice, diagnosis, or treatment.

---

## Developer

Developed by **Palash Chal**