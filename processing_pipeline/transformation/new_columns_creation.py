import pandas as pd
from utils import save_processed_data, get_saved_file_path, get_upstream_tasks_output_concat_df
from constants import X, Y, XY, TASK

"""
This is just an example code for a simple transformation task
"""
def create_xy_column(**context):
    df = get_upstream_tasks_output_concat_df(context, remove_none_values=True)
    xy_series = df[X].astype(str) + "/" + df[Y].astype(str)
    xy_df = pd.DataFrame(xy_series, columns=[XY])

    saved_file_path = get_saved_file_path(context[TASK].task_id)
    save_processed_data(xy_df, saved_file_path, use_index=False)
    return saved_file_path
