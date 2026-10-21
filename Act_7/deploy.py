import json

from azureml.core import Workspace
from azureml.core.model import Model
from azureml.core.environment import Environment
from azureml.core.conda_dependencies import CondaDependencies
from azureml.core.model import InferenceConfig
from azureml.core.webservice import AciWebservice


def deploy_model():

    with open("my_id.json", "r") as f:
        subscription = json.load(f)

    ws = Workspace.create(
        name="price_prediction",
        subscription_id=subscription["my_id"],
        resource_group="__hw1__",
        location="swedencentral",
        exist_ok=True
    )

    registered_model = Model.register(
        model_path="predict_price.pkl",
        model_name="price_prediction",
        workspace=ws
    )

    virtual_env = Environment("env-4-pricing")

    virtual_env.python.conda_dependencies = CondaDependencies.create(
        conda_packages=[
            "pandas",
            "scikit-learn"
        ],
        pip_packages=[
            "azureml-defaults"
        ]
    )

    inference_config = InferenceConfig(
        environment=virtual_env,
        entry_script="score.py"
    )

    aci_config = AciWebservice.deploy_configuration(
        cpu_cores=0.5,
        memory_gb=1
    )

    service = Model.deploy(
        workspace=ws,
        name="pricing-service",
        models=[registered_model],
        inference_config=inference_config,
        deployment_config=aci_config,
        overwrite=True
    )

    service.wait_for_deployment(show_output=True)

    return service.scoring_uri