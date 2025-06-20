from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os
import sys


sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pipelines.reddit_pipeline import *
from pipelines.aws_s3_pipeline import *

default_args = {
    'owner':"Hoang",
    'start_date': datetime(year=2025, month=6, day=19)

}

file_postfix = datetime.now().strftime("%Y%m%d")
s3_key = f'data/reddit_{file_postfix}reddit_data.csv'

with DAG(
    dag_id='etl_reddit_pipeline',
    default_args=default_args,
    schedule='@daily',
    catchup=False,
    tags=['reddit','etl','aws']
) as dag:

#exact from reddit 
    extract = PythonOperator(
        task_id = 'reddit_extraction',
        python_callable= reddit_pipeline,
        op_kwargs = {
            'file_name': f'reddit_{file_postfix}',
            'subreddit':'dataengineering',
            'time_filter':'day',
            'limit':10
        },
    )
#updload 
    upload = PythonOperator(
        task_id = 'upload_to_s3',
        python_callable = aws_pipeline,
    )

#run
    extract >> upload