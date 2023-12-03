from flask import Flask, request, render_template 
import joblib
import numpy as np


app = Flask(__name__)

flower_model = joblib.load("iris_model.pkl")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.form
        features = [float(data['sepal_length']), float(data['sepal_width']), float(data['petal_length']), float(data['petal_width'])]
        prediction = flower_model.predict([features])[0]
        return render_template('result.html', prediction=f'Predicted Class: {prediction}')
    except Exception as e:
        return render_template('result.html', prediction=f'Error: {str(e)}')




if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0' ,port=5000)