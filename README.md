# Diabetes Prediction Project

## Project Overview
The Diabetes Prediction Project is designed to predict the likelihood of diabetes in individuals based on key health metrics such as glucose levels, BMI, age, blood pressure, and insulin levels. Early prediction can help in preventive care and lifestyle management.

## Features
- User-friendly interface for inputting health parameters
- Predicts diabetes risk using machine learning
- Provides quick results for early detection

## Dataset
The project uses the **Pima Indians Diabetes Dataset**, which contains medical diagnostic measurements for female patients aged 21 and above. Key features include:
- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age
- Outcome (0 = No Diabetes, 1 = Diabetes)

## Model Used
The project uses **Logistic Regression**, a supervised machine learning algorithm suitable for binary classification problems.  

### Technical Details:
- **Algorithm:** Logistic Regression
- **Purpose:** Binary classification (Diabetes: Yes/No)
- **Libraries Used:** 
  - `pandas` for data manipulation
  - `numpy` for numerical operations
  - `scikit-learn` for machine learning models
- **Preprocessing Steps:**
  - Handling missing values
  - Feature scaling using `StandardScaler`
  - Splitting data into training and testing sets
- **Model Evaluation:**
  - Accuracy Score
  - Confusion Matrix
  - Precision, Recall, F1-Score

## How to Run
1. Clone the repository
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
python app.py
Open your browser and navigate to http://127.0.0.1:5000

Enter health parameters to get the diabetes prediction.
