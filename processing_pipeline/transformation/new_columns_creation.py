import pandas as pd
from utils import load_data, save_processed_data
from constants import X, Y, XY

"""
This is just an example code for a simple transformation task
"""
def create_xy_column(x_column_file_name, y_column_file_name):
    x_df = load_data(x_column_file_name, processed_data=True)
    y_df = load_data(y_column_file_name, processed_data=True)
    df = pd.concat([x_df, y_df])
    xy_series = df.apply(lambda row: "/".join(row[[X, Y]].astype(str)), axis=1)
    xy_df = pd.DataFrame(xy_series, columns=[XY])
    save_processed_data(xy_df,
                        process_name=f"create_xy_column",
                        use_index=False)
