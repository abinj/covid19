import os
from datetime import timedelta, datetime

# [START import_module]
# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
# Operators; we need this to operate!
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

# [END import_module]

# [START default_args]
# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization

format = "%a, %d %b %Y %H:%M:%S %Z"


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'default_timezone': "EST",
    'start_date': datetime(2020, 3, 19),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(hours=1),
    'schedule_interval': '@daily',
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'sla_miss_callback': yet_another_function,
    # 'trigger_rule': 'all_success'
}
# [END default_args]

# [START instantiate_dag]
dag = DAG(
    'news_fetch2',
    default_args=default_args,
    description='News Fetch DAG',
)
# [END instantiate_dag]

# t1 and t2 are examples of tasks created by instantiating operators
# [START basic_task]
t1 = BashOperator(
    task_id='fox_news_parser',
    depends_on_past=False,
    bash_command="python scripts/canada_covid_updates.py",
    # retries=3,
    dag=dag,
)

# t2 = BashOperator(
#     task_id='cnn_news_parser',
#     depends_on_past=False,
#     bash_command=rss_feed_scraper,
#     # retries=3,
#     dag=dag,
# )


# [END basic_task]

# [START documentation]
# dag.doc_md = __doc__
#
# t1.doc_md = """\
# #### Task Documentation
# You can document your task using the attributes `doc_md` (markdown),
# `doc` (plain text), `doc_rst`, `doc_json`, `doc_yaml` which gets
# rendered in the UI's Task Instance Details page.
# ![img](http://montcs.bloomu.edu/~bobmon/Semesters/2012-01/491/import%20soul.png)
# """
# [END documentation]

# [START jinja_template]
# templated_command = """
# {% for i in range(5) %}
#     echo "{{ ds }}"
#     echo "{{ macros.ds_add(ds, 7)}}"
#     echo "{{ params.my_param }}"
# {% endfor %}
# """
#
# t3 = BashOperator(
#     task_id='templated',
#     depends_on_past=False,
#     bash_command=templated_command,
#     params={'my_param': 'Parameter I passed in'},
#     dag=dag,
# )
# [END jinja_template]
#
# t1, t2
# [END tutorial]
# t1, t2