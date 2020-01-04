from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

import transformation


dag = DAG('anyway_processing_pipeline', start_date=datetime(2020, 1, 1))

transformation__create_xy_column = PythonOperator(task_id='transformation__create_xy_column',
                                                  python_callable=transformation.create_xy_column,
                                                  op_kwargs={"data_date_string": "20191161"},
                                                  dag=dag)
