# Smart Irrigation System (AI-Based)

This is a Python-based Smart Irrigation System that uses a Machine Learning model to automate water pumping decisions based on environmental conditions like temperature and soil moisture.

---

## Features

- Trained using a Decision Tree Classifier
- Takes `temperature` and `soil moisture` as input
- Predicts whether to turn the water pump **ON** or **OFF**
- Easily integrable with Arduino and sensor devices

---

## AI Model

- **Algorithm**: Decision Tree Classifier (via `scikit-learn`)
- **Input Features**: Temperature, Soil Moisture
- **Output**: 1 (Pump ON), 0 (Pump OFF)

---

## Project Structure

smart-irrigation-system/
├── ai_model/
│ ├── train_model.py # Trains the ML model
│ ├── irrigation_model.pkl # Saved model
│ └── irrigation_data.csv # Simulated training data
├── integration/
│ └── serial_predict.py # Uses model for real-time predictions
├── README.md # This file


---

## Install requirement

pip install pandas scikit-learn joblib
                or
pip install pandas
pip install scikit-learn
pip install joblib

---

## Train the model

cd smart-irrigation-system
cd ai_model
python train_model.py

---

##  Run Predictions

python smart-irrigation-system/integration/serial_predict.py

---

## Output Example

Temperature: 31, Soil: 250 => Pump: ON
Temperature: 25, Soil: 600 => Pump: OFF

---

## To do

Add real sensor data via Arduino serial input
Add humidity as an input feature
Deploy using Flask or FastAPI
Front-end dashboard

---

## Tech Stack

Python 3.10+
scikit-learn
pandas
joblib
VS Code