from fastapi import FastAPI
from pydantic import BaseModel
import pickle
from train_model import deploy_model
import os

if os.path.exists('model.pkl'):
    print("MODEL FOUND!")
else:
    train_X = ["good product", "bad service", "excellent", "terrible"]
    train_y = [1, 0, 1, 0]
    deploy_model(train_X, train_y)


app = FastAPI()

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)


class InputData(BaseModel):
    text: str

@app.post("/predict")
def predict(data: InputData): ## Equivalente a su score.py
    
    X = vectorizer.transform([data.text])

    # Predict
    pred = model.predict(X)[0]
    prob = model.predict_proba(X)[0][1]

    return {
        "prediction": str(pred),
        "probability": float(prob)
    }