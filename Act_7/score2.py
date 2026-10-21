import json
import pickle
import pandas as pd
import os

from azureml.core.model import Model


def init():
    global model

    model_path = Model.get_model_path("date_prediction")

    print("Model path:", model_path)
    print("Exists:", os.path.exists(model_path))

    with open(model_path, "rb") as f:
        model = pickle.load(f)

    print("MODEL LOADED SUCCESSFULLY")


def run(raw_data):
    try:
        data = json.loads(raw_data)

        if isinstance(data, dict):
            data = [data]

        data = pd.DataFrame(data)

        prediction = model.predict(data)

        return json.dumps({
            "result": prediction.tolist()
        })

    except Exception as e:
        return json.dumps({
            "error": str(e)
        })


