#install dependenices 
#python3 -m pip install apache-airflow

#import libraries
from datetime import timedelta
from datetime import datetime
from airflow import DAG  
from airflow.operators.python import PythonOperator 

from Loadsqldb import run_my_script
from loadtopost import run_my_script2
from truncate import run_my_script3



#set the default_arguments
default_args = {
    'owner': 'Davvy',
    'start_date': datetime(2025, 10, 23),
    'email_on_failure': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=30),
}

dag=DAG(
    'csv_to_databases',
    description= "Moving csv data into MYSQL database and then querying that data into a new table in POSTGRE database.",
    default_args=default_args,
    schedule_interval=timedelta(days=1) 
)

task1=PythonOperator(
    task_id='load_csv_to_mysqldb',
    python_callable= run_my_script,
    dag=dag,
)

task2=PythonOperator(
    task_id='load_mysqldb_data_into_postgredb',
    python_callable= run_my_script2,
    dag=dag,
)

task3=PythonOperator(
    task_id='truncate_all_data_from_both_databases',
    python_callable= run_my_script3,
    dag=dag,
)

#Task flow

task1 >> task2 >> task3 