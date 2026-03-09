import pickle
import numpy as np

# Load trained model
model = pickle.load(open("models/rainfall_model.pkl", "rb"))

print("Enter Weather Details")

MinTemp = float(input("Min Temperature: "))
MaxTemp = float(input("Max Temperature: "))
Humidity9am = float(input("Humidity at 9AM: "))
Humidity3pm = float(input("Humidity at 3PM: "))
Pressure9am = float(input("Pressure at 9AM: "))
Pressure3pm = float(input("Pressure at 3PM: "))
RainToday = int(input("Did it rain today? (1=Yes, 0=No): "))

input_data = np.array([[MinTemp, MaxTemp, Humidity9am, Humidity3pm, Pressure9am, Pressure3pm, RainToday]])

prediction = model.predict(input_data)

if prediction == 1:
    print("Rain Expected Tomorrow ☔")
else:
    print("No Rain Tomorrow ☀")