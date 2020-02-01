from pathlib import Path
from utils import save_processed_data, get_saved_file_path, get_upstream_tasks_output_concat_df
from constants import X, Y, XY, TASK


# TODO This is just an example code for a simple transformation task
def create_xy_column(**context) -> Path:
    df = get_upstream_tasks_output_concat_df(context, remove_none_values=True)
    xy_series = df[X].astype(str) + "/" + df[Y].astype(str)
    xy_series.name = XY

    saved_file_path = get_saved_file_path(context[TASK].task_id)
    save_processed_data(xy_series, saved_file_path, use_index=False)
    return saved_file_path
