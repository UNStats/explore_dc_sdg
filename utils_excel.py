import pandas as pd
import numpy as np


def write_to_excel(df, path, sheet_name, max_width):
    with pd.ExcelWriter(path,engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name=sheet_name, index=False)
        workbook = writer.book
        worksheet = writer.sheets[sheet_name]
        for i, col in enumerate(df.columns):
            col_width = max(min( max([len(str(val)) for val in df[col]]) + 4, max_width), 16)
            set_cols = worksheet.set_column(i, i, col_width)