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
    dag_id="3CUNJujuy_empty",
    start_date=datetime(2022, 11, 3),
    max_active_runs=5,
    schedule_interval="@hourly",
    default_args=default_args,
    catchup=False,
) as dag:

    @task()
    def jujuy_extract():
        return "Extract"

    @task()
    def jujuy_transform():
        return "Transform"

    @task()
    def jujuy_load():
        return "Load"

    jujuy_extract() >> jujuy_transform() >> jujuy_load()
