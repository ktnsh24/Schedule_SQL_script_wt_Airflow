from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import datetime
from datetime import timedelta
from datetime import datetime
import pandas as pd
import requests
import datetime
from datetime import date
import time
from date_callable_script import date_callable


default_arg = {'owner': 'airflow',
               'start_date': '2021-03-26',
               }
print("executing DAG")
dag = DAG('pythonfile',
          default_args=default_arg,
          schedule_interval='0 * * * *',
          catchup=False)
# 0 0 * * *

python_task = PythonOperator(dag=dag,
                             task_id='python_task',
                             python_callable=date_callable)
print("to_execute")
python_task
