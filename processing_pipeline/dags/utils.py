import pandas as pd
from pathlib import Path
import yaml

PROCESSING_PIPELINE_DAGS_FOLDER_PATH = Path(__file__).parent
RAW_DATA_CSV_FILES_PATH = Path(PROCESSING_PIPELINE_DAGS_FOLDER_PATH, "csv_files", "raw_csv_files")
RAW_DATA_CSV_FILES_PATH.mkdir(exist_ok=True, parents=True)
PROCESSED_DATA_CSV_FILES_PATH = Path(PROCESSING_PIPELINE_DAGS_FOLDER_PATH, "csv_files", "processed_csv_files")
PROCESSED_DATA_CSV_FILES_PATH.mkdir(exist_ok=True, parents=True)
FINAL_PROCESSED_DATA_CSV_FILES_PATH = Path(PROCESSING_PIPELINE_DAGS_FOLDER_PATH, "csv_files", "final_processed_csv_files")
FINAL_PROCESSED_DATA_CSV_FILES_PATH.mkdir(exist_ok=True, parents=True)

with Path(PROCESSING_PIPELINE_DAGS_FOLDER_PATH, "pipeline_configuration.yaml").open() as pipeline_configuration_file:
    pipeline_configuration = yaml.load(pipeline_configuration_file)

DATA_DATE_STRING = pipeline_configuration["data_date_string"]


def load_data(raw_data=False, processed_data=False):
    if raw_data and processed_data:
        raise ValueError("arguments 'raw_data' and 'processed_data' can't be both True")
    if not raw_data and not processed_data:
        raise ValueError("arguments 'raw_data' and 'processed_data' can't be both False")

    if raw_data:
        csv_files_path = RAW_DATA_CSV_FILES_PATH
    else:  # processed_data == True
        csv_files_path = PROCESSED_DATA_CSV_FILES_PATH

    file_name = "klali_14Nov_1539_AccData.csv"  # TODO change this to be an argument
    file_path = Path(csv_files_path, f"H{DATA_DATE_STRING}", file_name)
    df = pd.read_csv(file_path)
    return df


def save_processed_data(df, process_name, use_index=True):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("df argument is suppose to be a pandas' DataFrame")
    saved_file_path = Path(PROCESSED_DATA_CSV_FILES_PATH, DATA_DATE_STRING, f"processed__{process_name}.csv")
    saved_file_path.parent.mkdir(exist_ok=True, parents=True)
    df.to_csv(saved_file_path, index=use_index)


def concat_processed_data(): # TODO currently in utils but should move to a better place
    processed_data_parts = []
    for file_path in PROCESSED_DATA_CSV_FILES_PATH.glob(f"{DATA_DATE_STRING}/*.csv"):
        saved_processed_data_part = pd.read_csv(file_path)
        processed_data_parts.append(saved_processed_data_part)

    processed_data = pd.concat(processed_data_parts, axis=1)
    saved_file_path = Path(FINAL_PROCESSED_DATA_CSV_FILES_PATH, f"processed__{DATA_DATE_STRING}.csv")
    processed_data.to_csv(saved_file_path, index=False)