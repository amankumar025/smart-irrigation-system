import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

df = pd.read_csv("irrigation_data.csv")

X = df[["temperature", "soil"]]
y = df["pump_status"]

model = DecisionTreeClassifier()
model.fit(X, y)

joblib.dump(model, "irrigation_model.pkl")
print("Model trained and saved as irrigation_model.pkl")
