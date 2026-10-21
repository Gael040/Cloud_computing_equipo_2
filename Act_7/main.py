from connection import get_data
from model import train_model
from deploy import deploy_model


def main():

    # 1. Obtener datos
    print("Obteniendo datos...")
    datos = get_data()

    # 2. Entrenar modelo
    print("Entrenando modelo...")
    train_model(datos)

    # 3. Deploy
    print("Desplegando modelo...")
    scoring_uri = deploy_model()

    print("Modelo desplegado correctamente.")
    print(scoring_uri)


if __name__ == "__main__":
    main()