import pandas as pd
from pathlib import Path
import yaml
from constants import TASK_INSTANCE, TASK

PROCESSING_PIPELINE_DAGS_FOLDER_PATH = Path(__file__).parent
RAW_DATA_CSV_FILES_PATH = Path(PROCESSING_PIPELINE_DAGS_FOLDER_PATH, "csv_files", "raw_csv_files")
RAW_DATA_CSV_FILES_PATH.mkdir(exist_ok=True, parents=True)
PROCESSED_DATA_CSV_FILES_PATH = Path(PROCESSING_PIPELINE_DAGS_FOLDER_PATH, "csv_files", "processed_csv_files")
PROCESSED_DATA_CSV_FILES_PATH.mkdir(exist_ok=True, parents=True)
FINAL_PROCESSED_DATA_CSV_FILES_PATH = Path(PROCESSING_PIPELINE_DAGS_FOLDER_PATH, "csv_files", "final_processed_csv_files")
FINAL_PROCESSED_DATA_CSV_FILES_PATH.mkdir(exist_ok=True, parents=True)

with Path(PROCESSING_PIPELINE_DAGS_FOLDER_PATH, "pipeline_configuration.yaml").open() as pipeline_configuration_file:
    pipeline_configuration = yaml.load(pipeline_configuration_file, Loader=yaml.BaseLoader)

DATA_DATE_STRING = pipeline_configuration["data_date_string"]


def load_data(file_name, raw_data=False, processed_data=False):
    if raw_data and processed_data:
        raise ValueError("arguments 'raw_data' and 'processed_data' can't be both True")
    if not raw_data and not processed_data:
        raise ValueError("arguments 'raw_data' and 'processed_data' can't be both False")

    if raw_data:
        csv_files_path = RAW_DATA_CSV_FILES_PATH
    else:  # processed_data == True
        csv_files_path = PROCESSED_DATA_CSV_FILES_PATH

    file_path = Path(csv_files_path, f"H{DATA_DATE_STRING}", file_name)
    df = pd.read_csv(file_path)
    return df


def get_saved_file_path(process_task_id):
    saved_file_path = Path(PROCESSED_DATA_CSV_FILES_PATH, DATA_DATE_STRING, f"processed__{process_task_id}.csv")
    saved_file_path.parent.mkdir(exist_ok=True, parents=True)
    return saved_file_path


def save_processed_data(df, saved_file_path, use_index=True):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("df argument is suppose to be a pandas' DataFrame")
    df.to_csv(saved_file_path, index=use_index)


def concat_processed_data():  # TODO currently in utils but should move to a better place
    processed_data_parts = []
    for file_path in PROCESSED_DATA_CSV_FILES_PATH.glob(f"{DATA_DATE_STRING}/*.csv"):
        saved_processed_data_part = pd.read_csv(file_path)
        processed_data_parts.append(saved_processed_data_part)

    processed_data = pd.concat(processed_data_parts, axis=1)
    saved_file_path = Path(FINAL_PROCESSED_DATA_CSV_FILES_PATH, f"processed__{DATA_DATE_STRING}.csv")
    processed_data.to_csv(saved_file_path, index=False)


def get_upstream_tasks_outputs(context, with_task_ids_as_keys=False, remove_none_values=False):
    task_ids = context[TASK].upstream_task_ids
    task_outputs = context[TASK_INSTANCE].xcom_pull(task_ids=task_ids)

    if with_task_ids_as_keys:
        task_id_to_task_output = {}
        for task_index, task_id in enumerate(task_ids):
            task_output = task_outputs[task_index]
            if remove_none_values and task_output is None:
                continue
            task_id_to_task_output[task_id] = task_output
        return task_id_to_task_output
    else:
        if remove_none_values:
            task_outputs = [task_output for task_output in task_outputs if task_output is not None]
        return task_outputs
