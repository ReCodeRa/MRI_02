# Inspired by: https://www.geeksforgeeks.org/how-to-merge-multiple-excel-files-into-a-single-files-with-python/

import pandas as pd
import glob
xl_path = "./MRI/res"
file_list = glob.glob(xl_path + "/*/*.xlsx")
print(file_list)

xl_merged = pd.DataFrame()
for xl_file in file_list:
    xl_red = pd.read_excel(xl_file)
    xl_merged = xl_merged.append(
      xl_red, ignore_index=True)
 
xl_merged.to_excel('res.xlsx', index=False)