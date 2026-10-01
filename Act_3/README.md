# Actividad 3 - Clasificación de Sentimiento con API

Este proyecto entrena un modelo de clasificación de sentimiento multiclase utilizando **TF-IDF** y **Regresión Logística**.

Las clases utilizadas son:

- `positive`
- `neutral`
- `negative`

## Instrucciones de uso

### Paso 1. Instalar dependencias

```bash
pip install pandas scikit-learn fastapi uvicorn requests
```

### Paso 2. Ejecutar el notebook de entrenamiento

Ejecutar el notebook correspondiente al preprocesamiento y entrenamiento del modelo.

Los datos se dividen en entrenamiento y prueba utilizando:

```python
train_test_split(
    features,
    labels,
    test_size=0.2,
    random_state=42,
    stratify=labels
)
```

El modelo utiliza:

- `TfidfVectorizer`
- `LogisticRegression`
- `prajjwal1/bert-tiny`


Al finalizar el entrenamiento se generan los archivos:

```text
model.pkl
vectorizer.pkl
```

### Paso 3. Levantar la API

Desde la carpeta del proyecto ejecutar:

```bash
uvicorn mian:app --reload
```
Si se quiere utilizar la instancia de bert_tiny , levantar la api con 
```bash
uvicorn main:app --reload
```
La API estará disponible localmente en:

```text
http://127.0.0.1:8000
```

La documentación automática puede consultarse en:

```text
http://127.0.0.1:8000/docs
```

### Paso 4. Realizar inferencia

Para hacer inferencia ejecutar el archivo o notebook `API.ipynb`.

Ejemplo:

```python
import requests

url = "http://127.0.0.1:8000/predict"

data = {
    "text": "this service is so amazing I could die!!"
}

response = requests.post(url, json=data)

print(response.json())
```

Una respuesta posible es:

```json
{
    "prediction": "positive"
}
```

Para probar otro texto solamente se debe modificar el valor de `"text"`.

## Archivos principales

```text
api.py
train_model.py
API.ipynb
model.pkl
vectorizer.pkl
README.md
```

## Especificaciones mínimas de software

- Python 3.10 o superior
- pandas
- scikit-learn
- FastAPI
- Uvicorn
- requests

## Flujo general

```text
Texto
  ↓
TF-IDF
  ↓
Regresión Logística
  ↓
positive / neutral / negative
  ↓
API
  ↓
Respuesta JSON
```
con mini-bert es :
```text
texto
 ↓
BERT tokenizer
 ↓
BERT Tiny
 ↓
logits
 ↓
softmax
 ↓
positive / neutral / negative
```
