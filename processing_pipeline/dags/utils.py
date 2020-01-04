import pandas as pd
from pathlib import Path


PROCESSING_PIPELINE_DAGS_FOLDER_PATH = Path(__file__).parent
RAW_DATA_CSV_FILES_PATH = Path(PROCESSING_PIPELINE_DAGS_FOLDER_PATH, "csv_files", "raw_csv_files")
RAW_DATA_CSV_FILES_PATH.mkdir(exist_ok=True, parents=True)
PROCESSED_DATA_CSV_FILES_PATH = Path(PROCESSING_PIPELINE_DAGS_FOLDER_PATH, "csv_files", "processed_csv_files")
PROCESSED_DATA_CSV_FILES_PATH.mkdir(exist_ok=True, parents=True)


def load_data(data_date_string, raw_data=False, processed_data=False):
    if raw_data and processed_data:
        raise ValueError("arguments 'raw_data' and 'processed_data' can't be both True")
    if not raw_data and not processed_data:
        raise ValueError("arguments 'raw_data' and 'processed_data' can't be both False")

    if raw_data:
        csv_files_path = RAW_DATA_CSV_FILES_PATH
    else:  # processed_data == True
        csv_files_path = PROCESSED_DATA_CSV_FILES_PATH

    file_name = "klali_14Nov_1539_AccData.csv"  # TODO change this to be an argument
    file_path = Path(csv_files_path, f"H{data_date_string}", file_name)
    df = pd.read_csv(file_path)
    return df