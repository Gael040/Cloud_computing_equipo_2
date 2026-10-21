# Azure ML Price Prediction API

Este proyecto entrena un modelo de regresión utilizando datos almacenados en **Azure SQL Database** y posteriormente lo despliega como un servicio web utilizando **Azure Machine Learning**.

## Estructura del proyecto

```text
project/
│
├── connection.py
├── model.py
├── score.py
├── deploy.py
├── main.py
├── test_api.py
├── requirements.txt
├── my_passwd.json
└── my_id.json
```

### Archivos principales

- `connection.py`: conexión con Azure SQL Database y extracción de los datos.
- `model.py`: entrenamiento y guardado del modelo.
- `score.py`: script utilizado por Azure ML para realizar inferencias.
- `deploy.py`: registro y despliegue del modelo en Azure Machine Learning.
- `main.py`: ejecuta el pipeline completo.
- `test_api.py`: ejemplo de cómo consumir la API una vez desplegada.

## Instalación

Clonar el repositorio:

```bash
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_REPOSITORIO>
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

También es necesario tener instalado **Microsoft ODBC Driver 18 for SQL Server**.

## Credenciales

Crear un archivo `my_passwd.json`:

```json
{
    "my_password": "TU_PASSWORD"
}
```

Y un archivo `my_id.json`:

```json
{
    "my_id": "TU_SUBSCRIPTION_ID"
}
```

Estos archivos contienen credenciales y **no deben subirse a GitHub**. Se recomienda agregarlos al `.gitignore`.

## Ejecutar el proyecto completo

Para obtener los datos, entrenar el modelo y desplegarlo en Azure:

```bash
python main.py
```

El flujo ejecutado es:

```text
Azure SQL
   ↓
connection.py
   ↓
model.py
   ↓
predict_price.pkl
   ↓
deploy.py
   ↓
score.py
   ↓
Azure ML Endpoint
```

Al finalizar el despliegue se mostrará el `scoring_uri` del servicio.

## Consumir la API

Si el modelo **ya está desplegado** y únicamente se desea realizar una predicción, no es necesario volver a ejecutar el entrenamiento ni el despliegue.

Se puede utilizar directamente el formato incluido en:

```text
test_api.py
```

Solo es necesario colocar el endpoint correspondiente:

```python
scoring_uri = "TU_URL_DE_AZURE"
```

y proporcionar los datos utilizando el mismo formato del ejemplo de `test_api.py`.

Después ejecutar:

```bash
python test_api.py
```

La API regresará la predicción de `LineTotal` para los datos enviados.