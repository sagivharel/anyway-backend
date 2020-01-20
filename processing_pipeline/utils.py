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


def load_data(file_name: str, raw_data=False, processed_data=False) -> pd.DataFrame:
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


def get_saved_file_path(process_task_id: str) -> Path:
    saved_file_path = Path(PROCESSED_DATA_CSV_FILES_PATH, DATA_DATE_STRING, f"processed__{process_task_id}.csv")
    saved_file_path.parent.mkdir(exist_ok=True, parents=True)
    return saved_file_path


def save_processed_data(df_or_series: (pd.DataFrame, pd.Series), saved_file_path: Path, use_index=True):
    if isinstance(df_or_series, pd.DataFrame):
        df_or_series.to_csv(saved_file_path, index=use_index)
    elif isinstance(df_or_series, pd.Series):
        df_or_series.to_csv(saved_file_path, header=True, index=use_index)
    else:
        raise ValueError("df argument is suppose to be a pandas' DataFrame or Series")


def concat_processed_data(**context):  # TODO currently in utils but should move to a better place
    processed_data = get_upstream_tasks_output_concat_df(context, remove_none_values=True)
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


def get_upstream_tasks_output_concat_df(context, with_task_ids_as_keys=False, remove_none_values=False):
    upstream_tasks_output_dfs = []
    for upstream_tasks_output_file_path in get_upstream_tasks_outputs(context,
                                                                      with_task_ids_as_keys,
                                                                      remove_none_values):
        upstream_tasks_output_df = load_data(upstream_tasks_output_file_path, processed_data=True)
        upstream_tasks_output_dfs.append(upstream_tasks_output_df)

    df = pd.concat(upstream_tasks_output_dfs, axis=1)
    return df


def leave_the_same_way(file_name: str, columns: (list, tuple), **context) -> Path:  # TODO rename this to a better function name
    df = load_data(file_name, raw_data=True)
    selected_columns_df = df[columns]

    saved_file_path = get_saved_file_path(context[TASK].task_id)
    save_processed_data(selected_columns_df, saved_file_path, use_index=False)
    return saved_file_path
