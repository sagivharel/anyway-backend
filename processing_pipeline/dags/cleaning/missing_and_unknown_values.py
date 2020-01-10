import pandas as pd
from utils import load_data, save_processed_data

"""
This is just an example code for a simple cleaning task
"""
def replace_minus_one_with_null(column_name):
    df = load_data(raw_data=True)
    clean_series = df[column_name].replace(-1, None)
    clean_df = pd.DataFrame(clean_series, columns=[column_name])
    save_processed_data(clean_df,
                        process_name=f"replace_minus_one_with_null__{column_name}",
                        use_index=False)