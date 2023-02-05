file = "/home/recodera/MRI_dasa/MRI_02/Loper/Loper/LosiActa.pdf"

def pdf_tab_id(file):
    from tabula import read_pdf
    from tabulate import tabulate
    import os
    import re
    import json
    
    ls_df = read_pdf(file, pages="all")
    r = re.compile(r"[01][.]{1}\d{2}")
    for count, tb in enumerate(ls_df):
        ls_df[count].to_csv('df_csv.csv')
        with open('df_csv.csv') as f:
            s = f.read()
        dec = re.findall(r, s)
        js_str = json.dumps(dec)
        jsonFile = open("id.json", "w")
        jsonFile.write(js_str)
        jsonFile.close()

pdf_tab_id(file)