# 🌧 Rainfall Prediction ML Project

A Machine Learning web application that predicts whether it will rain tomorrow based on weather parameters.

This project uses a **Random Forest Classifier** and provides a **Flask web interface** for predictions.

---

# 🚀 Features

- Data preprocessing and cleaning
- Exploratory Data Analysis (EDA)
- Random Forest Machine Learning model
- Model evaluation
- Feature importance visualization
- Flask web application
- Responsive UI for rainfall prediction

---

# 📂 Project Structure

```
Rainfall_Prediction_Project
│
├── app
│   ├── app.py
│   └── templates
│       └── index.html
│
├── dataset
│   └── rainfall_data.csv
│
├── models
│   └── rainfall_model.pkl   (placeholder – generated after training)
│
├── notebooks
│   └── analysis.ipynb
│
├── src
│   ├── predict.py
│   └── train_model.py
│
├── requirements.txt
└── README.md
```

---

# ⚠️ Important Note

The trained model file **rainfall_model.pkl** is not included in this repository because it exceeds GitHub's file size limit.

You must **train the model locally** before running the application.

---

# 🛠 Installation Guide

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Rainfall_Prediction_Project.git
```

Navigate to the project folder:

```bash
cd Rainfall_Prediction_Project
```

---

# 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate the environment

### Windows

```bash
venv\Scripts\activate
```

### Mac / Linux

```bash
source venv/bin/activate
```

---

# 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 4️⃣ Train the Machine Learning Model

Before running the app, generate the trained model file.

### Option A — Run Notebook

Open the notebook:

```
notebooks/analysis.ipynb
```

Run **all cells**.

This will generate:

```
models/rainfall_model.pkl
```

---

### Option B — Run Training Script

```bash
python src/train_model.py
```

This will also create the trained model file:

```
models/rainfall_model.pkl
```

---

# 5️⃣ Run the Web Application

```bash
python app/app.py
```

You should see:

```
Running on http://127.0.0.1:5000
```

Open this in your browser:

```
http://127.0.0.1:5000
```

---

# 🌐 Using the Web App

Enter the following parameters:

| Feature | Description |
|-------|-------------|
MinTemp | Minimum Temperature |
MaxTemp | Maximum Temperature |
Humidity9am | Humidity at 9 AM |
Humidity3pm | Humidity at 3 PM |
Pressure9am | Atmospheric Pressure at 9 AM |
Pressure3pm | Atmospheric Pressure at 3 PM |
RainToday | Rain today (1 = Yes, 0 = No) |

Click **Predict** to see whether rain is expected tomorrow.

---

# 🧠 Machine Learning Model

Algorithm used:

```
Random Forest Classifier
```

Evaluation metrics used:

- Accuracy
- Confusion Matrix
- Classification Report
- Feature Importance

---

# 📊 Dataset

Dataset contains weather attributes such as:

- Temperature
- Humidity
- Atmospheric Pressure
- Rain occurrence

Dataset file:

```
dataset/rainfall_data.csv
```

---

# 🖥 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Flask
- HTML / CSS

---

# 📌 Future Improvements

- Deploy the project online
- Integrate real-time weather APIs
- Add rainfall probability prediction
- Improve UI with charts and analytics

---

# 👨‍💻 Author

**Kameswar Panda**

Machine Learning & Software Development

---

# ⭐ If you found this project useful, please give it a star!

