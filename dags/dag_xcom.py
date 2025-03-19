"""

xcom push and pull are used to retrive values from one task to another   i.e., data sharing


dont use xcoms for larger data volumes ;  eg : pandas data frame. otherwise it will crash

max size is 48 kb

"""






from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator


default_args = {
    'owner': 'naveen',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}


def greet(some_dict, ti):
    print("some dict: ", some_dict)
    first_name = ti.xcom_pull(task_ids='get_name', key='first_name')
    last_name = ti.xcom_pull(task_ids='get_name', key='last_name')
    age = ti.xcom_pull(task_ids='get_age', key='age')
    # age = ti.xcom_pull(task_ids='get_age')  -- for one return value
    print(f"Hello World! My name is {first_name} {last_name}, "
          f"and I am {age} years old!")


def get_name(ti):
    ti.xcom_push(key='first_name', value='Naveen')
    ti.xcom_push(key='last_name', value='kumar')


def get_age(ti):
    ti.xcom_push(key='age', value=25)


# def get_age():
#     return 20    -- for one return value


with DAG(
    default_args=default_args,
    dag_id='xcom_dag_v01',
    description='Our first dag using python operator',
    start_date=datetime(2025, 3, 3),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet,
        op_kwargs={'some_dict': {'a': 1, 'b': 2}}
    )

    task2 = PythonOperator(
        task_id='get_name',
        python_callable=get_name
    )

    task3 = PythonOperator(
        task_id='get_age',
        python_callable=get_age
    )

    [task2, task3] >> task1
