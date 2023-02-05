file = "/home/recodera/MRI_dasa/MRI_02/Loper/Loper/LosiActa.pdf"

def pdf_tab_id(file):
    from tabula import read_pdf
    from tabulate import tabulate
    import os
    import re
    
    ls_df = read_pdf(file, pages="all")
    r = re.compile(r"[01][.]{1}\d{2}")
    for count, tb in enumerate(ls_df):
        ls_df[count].to_csv('df_csv.csv')
        with open('df_csv.csv') as f:
            s = f.read()
        dec = re.findall(r, s)
        print(dec)

pdf_tab_id(file)