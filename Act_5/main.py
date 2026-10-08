from fastapi import FastAPI
from pydantic import BaseModel

from transformers import BertTokenizer, BertForSequenceClassification
import torch
import os


MODEL_PATH = "./sentiment_model"

app = FastAPI()


# Cargar tokenizer y modelo entrenado
tokenizer = BertTokenizer.from_pretrained(MODEL_PATH)

model = BertForSequenceClassification.from_pretrained(
    MODEL_PATH
)

model.eval()


# Mapeo de clases
id_to_label = {
    0: "negative",
    1: "neutral",
    2: "positive"
}


class InputData(BaseModel):
    text: str


@app.post("/predict")
def predict(data: InputData):

    # Tokenizar texto
    inputs = tokenizer(
        data.text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128
    )

    # Inferencia sin calcular gradientes
    with torch.no_grad():
        outputs = model(**inputs)

    # Scores del modelo
    logits = outputs.logits

    # Convertir scores a probabilidades
    probabilities = torch.softmax(logits, dim=1)

    # Clase con mayor probabilidad
    pred_id = torch.argmax(probabilities, dim=1).item()

    # Probabilidad de la clase predicha
    probability = probabilities[0][pred_id].item()

    return {
        "prediction": id_to_label[pred_id],
        "probability": float(probability)
    }