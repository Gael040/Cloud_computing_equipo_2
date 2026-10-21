import json
from pathlib import Path
import pandas as pd
import requests


id = open('service-uri.json', 'r')
mi = json.load(id)

scoring_uri = mi["scoring_uri"]


prueba = pd.DataFrame([
    {
        "CustomerID": 100,
        "NameStyle": 0,
        "Title": 0,
        "FirstName": 0,
        "MiddleName": 0,
        "LastName": 0,
        "Suffix": 0,
        "CompanyName": 0,
        "SalesPerson": 0,
        "EmailAddress": 0,
        "Phone": 0,
        "PasswordHash": 0,
        "PasswordSalt": 0,
        "rowguid": 0,
    }
])

headers = {
    "Content-Type": "application/json"
}


response = requests.post(
    scoring_uri,
    data=prueba.to_json(orient="records"),
    headers=headers
)


if response.status_code == 200:

    result = json.loads(response.json())

    if "error" in result:
        print("Error del modelo:")
        print(result["error"])

    else:
        fecha = pd.to_datetime(result["result"])

        print("Predicción:")
        print(fecha)
