import os
import joblib
import pandas as pd

# Get the path to the trained model
base_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(base_dir, '..', 'ai_model', 'irrigation_model.pkl')

# Load the trained model
model = joblib.load(model_path)

# Sample inputs [temperature, soil]
test_data = [
    [31, 250],
    [25, 600],
    [28, 300]
]

# Match feature names exactly as in training
columns = ["temperature", "soil"]

for sample in test_data:
    input_df = pd.DataFrame([sample], columns=columns)
    prediction = model.predict(input_df)
    
    pump_status = "ON" if prediction[0] == 1 else "OFF"
    print(f"Temperature: {sample[0]}, Soil: {sample[1]} => Pump: {pump_status}")