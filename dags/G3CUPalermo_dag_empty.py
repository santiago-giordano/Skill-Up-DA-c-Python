import os
import logging
import csv
import boto3
import pandas as pd
from datetime import date, datetime, timedelta
from airflow.models import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.decorators import dag, task

# Default settings applied to all tasks
default_args = {
    "owner": "P3",
    "retries": 5,
    "retry_delay": timedelta(minutes=1),
}

# Instantiate DAG
with DAG(
    dag_id="3CUPalermo_empty",
    start_date=datetime(2022, 11, 3),
    max_active_runs=5,
    schedule_interval="@hourly",
    default_args=default_args,
    catchup=False,
) as dag:

    @task()
    def palermo_extract():
        return "Extract"

    @task()
    def palermo_transform():
        return "Transform"

    @task()
    def palermo_load():
        return "Load"

    palermo_extract() >> palermo_transform() >> palermo_load()
