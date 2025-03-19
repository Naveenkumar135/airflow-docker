import logging
from airflow import DAG
from datetime import datetime, timedelta
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.operators.python import PythonOperator


# Change these to your identifiers, if needed.
POSTGRES_CONN_ID = "postgres_localhost"



def pg_extract(copy_sql):
  pg_hook = PostgresHook.get_hook(POSTGRES_CONN_ID)
  logging.info("Exporting query to file")
  pg_hook.copy_expert(copy_sql,filename = "/opt/airflow/data/pg_extract.csv")

 
with DAG(
dag_id="pg_extract",
start_date=datetime(2025, 3, 10),
schedule_interval=timedelta(days=1),
catchup=False,
) as dag:

  t1 = PythonOperator(
    task_id="pg_extract_task",
    python_callable=pg_extract,
    op_kwargs={
        "copy_sql": "COPY (SELECT * FROM dag_runs) TO STDOUT WITH CSV HEADER"
        }
    )
 
  t1