from datetime import datetime

import os
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from constants import MAHOZ

from transformation.new_columns_creation import create_xy_column
from cleaning.missing_and_unknown_values import replace_minus_one_with_null
from utils import concat_processed_data

DATA_DATE_STRING = "20191161"

dag = DAG('anyway_processing_pipeline', start_date=datetime(2020, 1, 1), concurrency=os.cpu_count(),
          default_args={"op_kwargs": {"data_date_string": DATA_DATE_STRING}})

transformation__create_xy_column = PythonOperator(task_id='transformation__create_xy_column',
                                                  python_callable=create_xy_column,
                                                  dag=dag)


cleaning__replace_minus_one_with_null__mahoz = PythonOperator(task_id='cleaning__replace_minus_one_with_null__mahoz',
                                                              python_callable=replace_minus_one_with_null,
                                                              op_kwargs={"column_name": MAHOZ},
                                                              dag=dag)


utils__concat_processed_data = PythonOperator(task_id='utils__concat_processed_data',
                                              python_callable=concat_processed_data,
                                              dag=dag)

transformation__create_xy_column.set_downstream(utils__concat_processed_data)
cleaning__replace_minus_one_with_null__mahoz.set_downstream(utils__concat_processed_data)