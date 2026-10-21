import json
import pickle
from pathlib import Path
from uuid import uuid4

import numpy as np
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from score2 import encode_features



def train_model(datos):

    features = datos.drop(columns=["ModifiedDate"]).copy()
    labels = pd.to_datetime(datos["ModifiedDate"], errors="raise", utc=True)

    X_train, X_test, y_train, y_test = train_test_split(
        features, labels, test_size=0.2, random_state=42
    )

    from sklearn.preprocessing import LabelEncoder
    label_encoders = {}

    features = datos.drop(columns=["ModifiedDate"]).copy()
    for columna in features.select_dtypes(exclude="number").columns:
        encoder = LabelEncoder()
        features[columna] = encoder.fit_transform(features[columna].astype(str))
        label_encoders[columna] = encoder

    from sklearn.linear_model import LinearRegression
    model = LinearRegression()
    model.fit(X_train, y_train)


    return model
