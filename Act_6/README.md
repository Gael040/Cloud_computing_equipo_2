# Actividad 6: aprendizaje federado

En esta actividad se entrenó una red neuronal convolucional para reconocer dígitos de MNIST. Se dividieron los datos en cuatro grupos para simular un entrenamiento federado y combinar su aprendizaje en un modelo global.

Se trabajaron dos formas de combinar los modelos: el promedio de pesos del notebook original y FedAdam, que actualiza el modelo global por rondas. También se incluyeron curvas de entrenamiento y validación para los grupos y el modelo global.

## Archivos

- **`fed.ipynb`**: notebook original con la carga de MNIST, el entrenamiento por grupos, el promedio de pesos y un entrenamiento centralizado como referencia.
- **`model.py`**: definición de la red convolucional con TensorFlow y Keras.
- **`local.ipynb`**: simulación de FedAdam con cuatro grupos, curvas de entrenamiento y validación, y evaluación del modelo global.
- **`requirements.txt`**: librerías necesarias para ejecutar el proyecto.
