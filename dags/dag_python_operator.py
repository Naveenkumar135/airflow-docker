from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator


default_args = {
    'owner': 'naveen',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}


def greet(first_name, age):
    print(f"Hello World! My name is {first_name}, "
          f"and I am {age} years old!")


with DAG(
    default_args=default_args,
    dag_id='our_dag_with_python_operator_v01',
    description='Our first dag using python operator',
    start_date=datetime(2025, 3, 1),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet,
        op_kwargs={"first_name":"naveen","age":25}
    )


    task1