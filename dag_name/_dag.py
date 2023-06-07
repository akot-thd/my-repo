"""
*Purpose*

...

*Outputs*

... :

-  `{view_1}`

"""

import os
from datetime import datetime, timedelta
from functools import partial

from airflow import DAG
from airflow.operators.dummy import DummyOperator

from composer_common.callbacks.airflow import notify_on_failure, notify_on_success
from composer_common.configuration import variables_yaml


BASE_DIR = os.path.dirname(__file__)

# Data Pipeline configuration
app_params = variables_yaml.get(
    app="dag_name",     # TODO Replace with the actual DAG name (which must be identical to the name in variables.yaml)
    variables_path=os.path.join(BASE_DIR, "variables.yaml")
)
secret_macros = variables_yaml.configure_secret_macros(variables=app_params)

# BigQuery-related configuration
PROJECT_ID, DATASETS = app_params['de_gcp_project_id'], app_params['datasets']
sources = variables_yaml.BigQuerySources(variables=app_params)
BASE_TABLES, STG_TABLES, VIEWS = sources.base_tables, sources.stg_tables, sources.views

# Task default arguments
default_args = {
    # Default parameters
    'depends_on_past': False,
    'provide_context': True,

    # Retries parameters
    'retries': 3,
    'retry_delay': timedelta(minutes=5),

    # Callbacks
    'on_failure_callback': partial(notify_on_failure, notify_in_slack=False, notify_in_datadog=True),

    # Environment details
    'env': app_params['env'],
}

with DAG(
        dag_id='dag_name',                                  # TODO Replace with the actual DAG name
        start_date=datetime(2023, 6, 6),                    # TODO Replace with actual start date
        catchup=False,
        schedule_interval='0 * * * *',                      # TODO Replace with actual schedule interval
        default_args=default_args,
        max_active_runs=1,
        is_paused_upon_creation=True,
        on_failure_callback=partial(notify_on_failure, notify_in_slack=True, notify_in_datadog=False),
        user_defined_macros=secret_macros,
        params=app_params,
        description="""Short description""",                # TODO Replace with actual short DAG description
) as dag:
    # TODO Fill the DOCSTRING above and use the actual arguments to parametrize the description in different envs.
    dag.doc_md = __doc__.format(
        view_1=VIEWS["ExampleSource"]["full_ref"],
    )

    t_start = DummyOperator(task_id="start")

    t_end = DummyOperator(
        task_id="end",
        on_success_callback=partial(notify_on_success, notify_in_slack=False, notify_in_datadog=True),
    )

    # TODO DAG code
    # ...

    t_start >> t_end
