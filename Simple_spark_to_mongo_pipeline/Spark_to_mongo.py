from datetime import datetime
from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

with DAG(
    dag_id="spark_to_mongo",
    start_date=datetime(2025, 1, 16),
    schedule=None,
    catchup=False,
) as dag:

    spark_to_mongo = SparkSubmitOperator(
        task_id="write_to_mongo",
        application="/data/spark/jobs/write_to_mongo.py",
        conn_id="spark_airflow",
        verbose=True,
    )
