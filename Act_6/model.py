"""CNN para MNIST compartida por los grupos y el servidor federado."""

import tensorflow as tf


def build_model(learning_rate=1e-3, optimizer="adam"):
    """CNN de fed.ipynb para clasificar los digitos de MNIST."""
    if learning_rate <= 0:
        raise ValueError("learning_rate debe ser mayor que cero.")
    if optimizer == "adam":
        local_optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate)
    elif optimizer == "sgd":
        local_optimizer = tf.keras.optimizers.SGD(learning_rate=learning_rate)
    else:
        raise ValueError("optimizer debe ser 'adam' o 'sgd'.")

    model = tf.keras.Sequential(
        [
            tf.keras.Input(shape=(28, 28, 1)),
            tf.keras.layers.Conv2D(32, (3, 3), activation="relu"),
            tf.keras.layers.MaxPooling2D((2, 2)),
            tf.keras.layers.Conv2D(64, (3, 3), activation="relu"),
            tf.keras.layers.MaxPooling2D((2, 2)),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(64, activation="relu"),
            tf.keras.layers.Dense(10, activation="softmax"),
        ],
        name="mnist_cnn",
    )
    model.compile(
        optimizer=local_optimizer,
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"],
    )
    return model


class build:
    """Para usar build.build_it() como en fed.ipynb."""

    build_it = staticmethod(build_model)


if __name__ == "__main__":
    build_model().summary()
