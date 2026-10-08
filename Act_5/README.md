# Sentiment Analysis API

API de análisis de sentimiento usando **FastAPI**, **BERT**, **Docker** y **Azure**.

Clases:
- `positive`
- `neutral`
- `negative`

## Ejecutar localmente

```bash
docker build -t act5-api .
docker run --rm -p 3100:3100 act5-api
```

Documentación Swagger:

```text
http://localhost:3100/docs
```

## API desplegada en Azure

Swagger:

```text
https://act5-api.victoriousbeach-13ddc51d.swedencentral.azurecontainerapps.io/docs
```

Endpoint:

```text
POST /predict
```

Ejemplo de uso:

```python
import requests

url = "https://act5-api.victoriousbeach-13ddc51d.swedencentral.azurecontainerapps.io/predict"

data = {
    "text": "this service is amazing, love it"
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())
```

También se incluye un notebook con un ejemplo de consumo de la API desplegada en Azure.

## Tecnologías

- FastAPI
- PyTorch
- Hugging Face Transformers
- Docker
- Azure Container Registry
- Azure Container Apps