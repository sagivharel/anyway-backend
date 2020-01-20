from pathlib import Path
from utils import load_data, save_processed_data, get_saved_file_path
from constants import TASK


# TODO This is just an example code for a simple cleaning task:
def replace_minus_one_with_null(file_name: str, column_name: str, **context) -> Path:
    df = load_data(file_name, raw_data=True)
    clean_series = df[column_name].replace(-1, None)

    saved_file_path = get_saved_file_path(context[TASK].task_id)
    save_processed_data(clean_series, saved_file_path, use_index=False)
    return saved_file_path
