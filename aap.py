from flask import Flask, render_template, request, flash,app
from flask import Response
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)

scaler = pickle.load(open('Model/StandardScaler.pkl', 'rb'))
model = pickle.load(open('Model/ModelPrediction.pkl', 'rb'))

# Route for Home Page

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])

def predict():
    result = ''
    if request.method == 'POST':

        Pregnancies = int(request.form.get('Pregnancies'))
        Glucose = float(request.form.get('Glucose'))
        BloodPressure = float(request.form.get('BloodPressure'))
        SkinThickness = float(request.form.get('SkinThickness'))
        Insulin = float(request.form.get('Insulin'))
        BMI = float(request.form.get('BMI'))
        DiabetesPedigreeFunction = float(request.form.get('DiabetesPedigreeFunction'))
        Age = int(request.form.get('Age'))

        new_data = scaler.transform([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        predict=model.predict(new_data)

        if predict[0]==1:
            result="Diabetic"
        else:
            result="Non-Diabetic"

        return render_template('Single_prediction.html', result=result)

    else:
        return render_template('Home.html')

if __name__ == '__main__':
    app.run(debug=True)
