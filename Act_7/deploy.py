import json
from pathlib import Path

from azureml.core import Workspace
from azureml.core.conda_dependencies import CondaDependencies
from azureml.core.environment import Environment
from azureml.core.model import InferenceConfig, Model
from azureml.core.webservice import AciWebservice

from score2 import load_artifact

BASE_DIR = Path(__file__).resolve().parent


def deploy_model():
    artifact_path = BASE_DIR / "date_prediction.pkl"
    artifact = load_artifact(artifact_path)
    with (BASE_DIR / "my_id.json").open() as f:
        subscription = json.load(f)
    ws = Workspace.get(
        name="date_prediction",
        subscription_id=subscription["my_id"],
        resource_group="__hw1__",
    )
    registered_model = Model.register(
        model_path=str(artifact_path), model_name="date_prediction", workspace=ws
    )
    virtual_env = Environment("env-4-date-prediction-v2")
    virtual_env.python.conda_dependencies = CondaDependencies.create(
        conda_packages=["python=3.11"],
        pip_packages=[
            "azureml-defaults",
            *[f"{package}=={version}" for package, version in artifact["versions"].items()],
        ],
    )
    inference_config = InferenceConfig(
        environment=virtual_env,
        entry_script=str(BASE_DIR / "score2.py"),
    )
    service = Model.deploy(
        workspace=ws,
        name="date-service",
        models=[registered_model],
        inference_config=inference_config,
        deployment_config=AciWebservice.deploy_configuration(cpu_cores=0.5, memory_gb=1),
        overwrite=True,
    )
    service.wait_for_deployment(show_output=True)
    with (BASE_DIR / "service-uri.json").open("w") as f:
        json.dump({"scoring_uri": service.scoring_uri}, f, indent=2)
    return service.scoring_uri
