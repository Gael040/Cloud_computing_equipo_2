import requests
import json
import pandas as pd


import json

id = open('service-uri.json', 'r')
mi = json.load(id)

scoring_uri = mi["scoring_uri"]


prueba = pd.DataFrame([

    {
        "SalesOrderID": 71774,
        "SalesOrderDetailID": 110562,
        "OrderQty": 1,
        "ProductID": 836,
        "UnitPrice": 356.898,
        "UnitPriceDiscount": 0
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
    print("result: ", result)
    prueba["LineTotal_Predicted"] = result["result"]

    print(prueba)

else:

    print(f"Error: {response.text}")