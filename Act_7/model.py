import pickle

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


def train_model(datos):

    df = datos.copy()

    features = df.drop(
        ["LineTotal", "rowguid", "ModifiedDate"],
        axis=1
    )

    labels = df["LineTotal"]

    X_train, X_test, y_train, y_test = train_test_split(
        features,
        labels,
        test_size=0.2,
        random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    pred = model.predict(X_test)

    r2 = r2_score(y_test, pred)

    print(f"R2: {r2:.4f}")

    with open("predict_price.pkl", "wb") as f:
        pickle.dump(model, f)

    return model