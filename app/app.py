from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("models/rainfall_model.pkl","rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    MinTemp = float(request.form["MinTemp"])
    MaxTemp = float(request.form["MaxTemp"])
    Humidity9am = float(request.form["Humidity9am"])
    Humidity3pm = float(request.form["Humidity3pm"])
    Pressure9am = float(request.form["Pressure9am"])
    Pressure3pm = float(request.form["Pressure3pm"])
    RainToday = int(request.form["RainToday"])

    features = np.array([[MinTemp,MaxTemp,Humidity9am,Humidity3pm,Pressure9am,Pressure3pm,RainToday]])

    prediction = model.predict(features)

    if prediction == 1:
        result = "Rain Expected Tomorrow ☔"
    else:
        result = "No Rain Tomorrow ☀"

    return render_template("index.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)