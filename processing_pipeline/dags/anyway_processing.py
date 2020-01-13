from datetime import datetime

import os
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from constants import MAHOZ, X, Y

from transformation.new_columns_creation import create_xy_column
from cleaning.missing_and_unknown_values import replace_minus_one_with_null
from utils import concat_processed_data


dag = DAG('anyway_processing_pipeline',
          schedule_interval=None,
          start_date=datetime(2020, 1, 1),
          concurrency=os.cpu_count())



cleaning__replace_minus_one_with_null__mahoz = PythonOperator(task_id='cleaning__replace_minus_one_with_null__mahoz',
                                                              python_callable=replace_minus_one_with_null,
                                                              op_kwargs={"file_name": "klali_08Jan_0930_AccData.csv",
                                                                         "column_name": MAHOZ},
                                                              dag=dag)

cleaning__replace_minus_one_with_null__y = PythonOperator(task_id='cleaning__replace_minus_one_with_null__y',
                                                          python_callable=replace_minus_one_with_null,
                                                          op_kwargs={"file_name": "klali_08Jan_0930_AccData.csv",
                                                                     "column_name": Y},
                                                          dag=dag)

cleaning__replace_minus_one_with_null__x = PythonOperator(task_id='cleaning__replace_minus_one_with_null__x',
                                                          python_callable=replace_minus_one_with_null,
                                                          op_kwargs={"file_name": "klali_08Jan_0930_AccData.csv",
                                                                     "column_name": X},
                                                          dag=dag)

transformation__create_xy_column = PythonOperator(task_id='transformation__create_xy_column',
                                                  python_callable=create_xy_column,
                                                  op_kwargs={
                                                      "x_column_file_name": "replace_minus_one_with_null__X.csv",
                                                      "y_column_file_name": "replace_minus_one_with_null__Y.csv"
                                                             },
                                                  dag=dag)

utils__concat_processed_data = PythonOperator(task_id='utils__concat_processed_data',
                                              python_callable=concat_processed_data,
                                              dag=dag)

cleaning__replace_minus_one_with_null__y.set_downstream(transformation__create_xy_column)
cleaning__replace_minus_one_with_null__x.set_downstream(transformation__create_xy_column)
transformation__create_xy_column.set_downstream(utils__concat_processed_data)
cleaning__replace_minus_one_with_null__mahoz.set_downstream(utils__concat_processed_data)