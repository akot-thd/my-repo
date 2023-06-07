from unittest.mock import patch

from airflow.models import DagBag

import pytest


@pytest.fixture
@patch("composer_common.configuration.variables_yaml.conf")
def prod_dag_bag(mocked_conf, dag_path):
    """
    Returns DagBag instance with added DAG.
    """
    mocked_conf.get.return_value = "prod"
    return DagBag(dag_folder=dag_path, include_examples=False)


@pytest.fixture
@patch("composer_common.configuration.variables_yaml.conf")
def dev_dag_bag(mocked_conf, dag_path):
    """
    Returns DagBag instance with added DAG.
    """
    mocked_conf.get.return_value = "dev"
    return DagBag(dag_folder=dag_path, include_examples=False)


@pytest.mark.unittest
def test_is_valid_production_dag(prod_dag_bag, prod_params):
    """
    Checks if DAG imports without errors.
    The test is equal to the test which Airflow does after adding a new DAG.
    """

    assert prod_dag_bag.import_errors == {}


@pytest.mark.unittest
def test_is_valid_development_dag(dev_dag_bag, prod_params):
    """
    Checks if DAG imports without errors.
    The test is equal to the test which Airflow does after adding a new DAG.
    """

    assert dev_dag_bag.import_errors == {}


@pytest.mark.unittest
def test_if_dag_has_description(prod_dag_bag, dag_id):
    """Checks if DAG has descriptions"""

    assert prod_dag_bag.dags[dag_id].description is not None
    assert prod_dag_bag.dags[dag_id].doc_md is not None


@pytest.mark.unittest
def test_if_dag_tasks_have_descriptions(prod_dag_bag, dag_id):
    """Checks if DAG tasks have descriptions."""

    no_description = list()
    for task in prod_dag_bag.dags[dag_id].tasks:
        if task.task_id not in {'start', 'end'} and not task.doc_md:
            no_description.append(task.task_id)

    assert no_description == []
