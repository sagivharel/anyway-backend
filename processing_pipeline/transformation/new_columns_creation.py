import pandas as pd
from utils import load_data, save_processed_data, get_upstream_tasks_outputs, get_saved_file_path
from constants import X, Y, XY, TASK

"""
This is just an example code for a simple transformation task
"""
def create_xy_column(**context):
    upstream_tasks_output_dfs = []
    for upstream_tasks_output_file_path in get_upstream_tasks_outputs(context, remove_none_values=True):
        upstream_tasks_output_df = load_data(upstream_tasks_output_file_path, processed_data=True)
        upstream_tasks_output_dfs.append(upstream_tasks_output_df)

    df = pd.concat(upstream_tasks_output_dfs)
    xy_series = df[X].astype(str) + "/" + df[Y].astype(str)
    xy_df = pd.DataFrame(xy_series, columns=[XY])

    saved_file_path = get_saved_file_path(context[TASK].task_id)
    save_processed_data(xy_df, saved_file_path, use_index=False)
    return saved_file_path
