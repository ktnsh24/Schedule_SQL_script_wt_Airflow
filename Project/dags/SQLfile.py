from airflow import DAG
from airflow.operators.mysql_operator import MySqlOperator
import datetime
from datetime import timedelta

default_arg = {'owner': 'airflow',
               'start_date': '2021-03-26'}
print("executing DAG")
dag = DAG('SQLfile',
          default_args=default_arg,
          schedule_interval='0 0 * * *',
          template_searchpath=['/Users/ketansahu/Documents/DataEngineeringProject/Scheduling_SQL_Airflow/Project/dags'])
# 0 0 * * *
print("toMySqlOpeartor")
mysql_task = MySqlOperator(dag=dag,
                           mysql_conn_id='mysql_default',
                           task_id='mysql_task',
                           sql='batch_schedular.sql')
print("to_execute")
mysql_task
