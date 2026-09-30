# Actividad 2 - Bankruptcy Prediction Deployment

Esta actividad entrena y despliega en Azure Machine Learning un modelo de clasificación binaria para predecir bancarrota.

## Archivos principales

- `Act_semana2.ipynb`: entrenamiento, registro y despliegue del modelo.
- `API(act2).ipynb`: consume el servicio desplegado y realiza inferencia.
- `score.py`: script de inferencia utilizado por Azure ML.
- `prueba.csv`: datos de ejemplo para probar la API.
- `service_uri.json`: contiene la URI del servicio desplegado.
- `logistic_regressor.pkl`: modelo entrenado.

## Instrucciones de uso

### Paso 1. Clonar el repositorio

```bash
git clone https://github.com/Gael040/Cloud_computing_equipo_2.git
```

Después, entrar a la carpeta de la actividad:

```bash
cd "Cloud_computing_equipo_2/Act 2"
```

### Paso 2. Instalar las dependencias necesarias

Instalar las principales librerías utilizadas:

```bash
pip install pandas numpy scikit-learn joblib requests azureml-core azureml-defaults
```

### Paso 3. Configurar el acceso a Azure

Crear un archivo local llamado:

```text
my_id.json
```

con la siguiente estructura:

```json
{
    "my_id": "TU_SUBSCRIPTION_ID"
}
```

Este archivo no se incluye en el repositorio público.

### Paso 4. Ejecutar el notebook principal

Abrir:

```text
Act_semana2.ipynb
```

y ejecutar todas las celdas en orden.

Este notebook realiza:

1. Carga y preparación de los datos.
2. División de datos en entrenamiento y prueba.
3. Entrenamiento del modelo `LogisticRegression`.
4. Evaluación del modelo.
5. Guardado del modelo como `logistic_regressor.pkl`.
6. Conexión con Azure Machine Learning.
7. Registro del modelo como `bankruptcy_model`.
8. Creación del ambiente de ejecución.
9. Generación de `score.py`.
10. Despliegue del modelo utilizando Azure Container Instances.

### Paso 5. Obtener la URI del servicio

Después del despliegue, Azure genera una URI para acceder al modelo.

Esta URI debe guardarse en:

```text
service_uri.json
```

con el siguiente formato:

```json
{
    "scoring_uri": "URI_DEL_SERVICIO"
}
```

### Paso 6. Preparar los datos de prueba

El archivo:

```text
prueba.csv
```

contiene datos de ejemplo para realizar inferencia.

Para utilizar nuevos datos, se puede sustituir este archivo por otro CSV que mantenga las mismas columnas utilizadas durante el entrenamiento.

La variable objetivo `Bankrupt?` no debe enviarse como característica de entrada al modelo.

### Paso 7. Ejecutar la API

Abrir:

```text
API(act2).ipynb
```

y ejecutar todas las celdas.

Este notebook:

1. Lee la URI desde `service_uri.json`.
2. Carga los datos de `prueba.csv`.
3. Convierte los datos a formato JSON.
4. Envía una petición HTTP POST al servicio desplegado.
5. Recibe las predicciones del modelo.
6. Agrega la predicción `Bankrupt?` al DataFrame.
7. Muestra los resultados.

### Paso 8. Interpretar el resultado

El modelo devuelve una clasificación binaria:

```text
0 = No se predice bancarrota
1 = Se predice bancarrota
```

## Uso rápido

Si el modelo ya se encuentra desplegado, no es necesario volver a ejecutar `Act_semana2.ipynb`.

Solo se necesita:

```text
API(act2).ipynb
prueba.csv
service_uri.json
```

Después:

1. Sustituir `prueba.csv` por los datos que se quieran consultar.
2. Ejecutar `API(act2).ipynb`.
3. Revisar las predicciones generadas por el modelo.

## Flujo general

```text
Datos
   ↓
Entrenamiento del modelo
   ↓
Registro en Azure Machine Learning
   ↓
Despliegue en Azure Container Instances
   ↓
service_uri.json
   ↓
API(act2).ipynb
   ↓
Predicción de Bankrupt?
```