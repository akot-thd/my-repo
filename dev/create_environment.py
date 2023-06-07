"""
This script is supposed to be used to create development tables in BigQuery.
"""

import os

from composer_common.configuration import variables_yaml
from composer_common.development.environment.bigquery import create_environment


DAG_ID = "dag_name"     # TODO: Replace with the actual DAG name (which must be identical to the folder name containing the DAG files).
REPO_DIR = os.path.dirname(os.path.dirname(__file__))
VARIABLES_PATH = os.path.join(REPO_DIR, DAG_ID, "variables.yaml")

prod_params = variables_yaml.get(app=DAG_ID, variables_path=VARIABLES_PATH, env="prod")
dev_params = variables_yaml.get(app=DAG_ID, variables_path=VARIABLES_PATH, env="dev")

create_environment(
    file_path="bigquery_env.sql",
    jinja_parameters={"prod": prod_params, "dev": dev_params},
)
