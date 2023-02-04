from tabula import read_pdf
from tabulate import tabulate
import os
# import camelot

file = "/home/recodera/MRI_dasa/MRI_02/Loper/Loper/LosiActa.pdf"

#reads table from pdf file
print(os.getcwd())
ls_df = read_pdf(file, pages="all") #address of pdf file
# print(tabulate(ls_df))

for tb in ls_df:
    # tb.info
    # print(list(tb.columns))
    # tb.head()
    # print(tb.between(0, 2, inclusive=True))
    # df_new = df.iloc[:, 0:3]
    df_str = tb.to_string()
    print(df_str)


df_str = ls_df[0].to_string()
print(df_str)

ls_df[0].to_csv('df_csv.csv')

## RegEx
import re
r = re.compile(r"[01][.]{1}\d{2}")
with open('df_csv.csv') as f:
    s = f.read()

dec = re.findall(r, s)
print(dec)


dec = 

# print(os.getcwd())
# pth = '/home/recodera/MRI_dasa/MRI_02/Loper/Loper/'
# os.chdir(pth)
# print(os.listdir())

# tables = camelot.read_pdf(file)