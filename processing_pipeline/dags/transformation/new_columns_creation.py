import pandas as pd
from utils import load_data, save_processed_data
from constants import X, Y

"""
This is just an example code for a simple transformation task
"""
def create_xy_column(data_date_string):
    df = load_data(data_date_string, raw_data=True)
    xy_series = df.apply(lambda row: "/".join(row[[X, Y]].astype(str)), axis=1)
    xy_df = pd.DataFrame(xy_series, columns=[f"{X}/{Y}".lower()])
    save_processed_data(xy_df,
                        data_date_string=data_date_string,
                        process_name=f"create_xy_column",
                        use_index=False)
