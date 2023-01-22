import pandas as pd
import glob
xl_path = "./MRI/res"
file_list = glob.glob(xl_path + "/*/*.xlsx")
print(file_list)