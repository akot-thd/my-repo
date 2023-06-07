import logging
import os

import pytest
from composer_common.configuration import variables_yaml


logging.getLogger('airflow.configuration').setLevel(logging.ERROR)  # to suppress warnings from this module


@pytest.fixture(scope="session")
def dag_id():
    return "dag_name"   # TODO Replace with the actual DAG folder name


@pytest.fixture(scope="session")
def dag_path(dag_id):
    """Creates a DAG path for tests"""

    repo_path = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(repo_path, dag_id)


@pytest.fixture(scope="session")
def tests_path():
    """Creates a test path for tests"""

    return os.path.dirname(__file__)


@pytest.fixture(scope="session")
def prod_params(dag_id, dag_path):
    variables_file = os.path.join(dag_path, "variables.yaml")
    return variables_yaml.get(app=dag_id, variables_path=variables_file, env="prod")


@pytest.fixture(scope="session")
def dev_params(dag_id, dag_path):
    variables_file = os.path.join(dag_path, "variables.yaml")
    return variables_yaml.get(app=dag_id, variables_path=variables_file, env="dev")
