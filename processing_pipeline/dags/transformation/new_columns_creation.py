from utils import load_data

"""
This is just an example code for a simple transformation task
"""
def create_xy_column(data_date_string):
    df = load_data(data_date_string, raw_data=True)
    xy_series = df.apply(lambda row: "/".join(row[["X", "Y"]].astype(str)), axis=1)
    return xy_series
