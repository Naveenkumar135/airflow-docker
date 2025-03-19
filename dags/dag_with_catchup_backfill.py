
"""
This catch up is useful when we dont want the tasks to be executed from start date
it will run from current execution date instead

if we want to execute manually from start date 

we need run these command 

docker exec -it < container_id_for_webserver > bash

airflow dags backfill -s 2025-03-01 -e 2025-03-03 dag_with_catchup_backfill_v01

exit
"""

from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'naveen',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='dag_with_catchup_backfill_v01',
    default_args=default_args,
    start_date=datetime(2025, 3, 4),
    schedule_interval='@daily',
    catchup=False
) as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command='echo This is a simple bash command!'
    )

    # docker build . --tag extending_airflow:latest