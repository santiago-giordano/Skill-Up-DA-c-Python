from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.dummy import DummyOperator

with DAG(
    'dag_grupo_universidades_b',
    description='DAG para la Universidad Nacional Del Comahue y Universidad Del Salvador',
    schedule_interval=timedelta(hours=1),
    start_date=datetime(2022, 11, 3)
) as dag:
    query_sql = DummyOperator(task_id='query_sql')
    pandas_process = DummyOperator(task_id='pandas_process')
    load_S3 = DummyOperator(task_id='load_S3')

    query_sql >> pandas_process >> load_S3