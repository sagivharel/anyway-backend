from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from utils import get_upstream_tasks_outputs

dag = DAG('processing_example',
          schedule_interval=None,
          start_date=datetime(2020, 1, 1))


def create_txt_file(**context):
    file_name = "testing_file"
    with open(f"{file_name}.txt", "w") as file:
        file.write("text")

    return file_name


def create_json_file(**context):
    file_name = "testing_json_file"
    with open(f"{file_name}.json", "w") as file:
        file.write("json")


def create_second_txt_file(file_name, **context):
    data = get_upstream_tasks_outputs(context, with_task_ids_as_keys=True, remove_none_values=False)
    with open(f"{file_name}.txt", "w") as file:
        file.write(str(data))


zero = PythonOperator(task_id="zero", python_callable=create_json_file, dag=dag, provide_context=True)
one = PythonOperator(task_id="one", python_callable=create_txt_file, dag=dag, provide_context=True)
two = PythonOperator(task_id="two", python_callable=create_second_txt_file, dag=dag, provide_context=True,
                     op_kwargs={"file_name": "testing_file2"})
three = PythonOperator(task_id="three", python_callable=create_second_txt_file, dag=dag, provide_context=True,
                       op_kwargs={"file_name": "testing_file_three"})


zero.set_downstream(two)
one.set_downstream(two)
two.set_downstream(three)
