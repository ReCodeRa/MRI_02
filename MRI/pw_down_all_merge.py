import os
import pandas as pd
from playwright.sync_api import sync_playwright
from itertools import chain
from pathlib import Path
import glob

timeout = 30 * 1000                  #  timeout

# Read IDs from .csv to ls
df = pd.read_csv('lsIDs.csv', delimiter=',')
lsls = [list(row) for row in df.values]
lsIDs = list(chain.from_iterable(lsls))
print(lsIDs[0:3])

def main(key):
    id_uds = key.replace('/', '_')
    os.makedirs(f'res/{id_uds}/', exist_ok=True)
   
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(f"https://mri.cts-mrp.eu/portal/details?productnumber={key}")
        
        with page.expect_download() as download_info:
            page.get_by_text("Download excel").click()
        download = download_info.value
        download.save_as(f"res/{id_uds}/{id_uds}.xlsx")    
        
        page.wait_for_selector('mat-card', timeout=timeout) # completely load the page
        downloads = page.locator('mat-card').locator("button")
        # texts = await downloads.all_text_contents() # just making sure I got what I thought I got
        count = downloads.count()
        print(f'There are {count} buttons in mat-card section.')

        for i in range(count):
            print(f"Starting download {i}")
            with page.expect_download() as download_handler:
                downloads.nth(i).click(timeout=0)
            download = download_handler.value
            doc_name = download.suggested_filename
            download.save_as(f"res/{id_uds}/{doc_name}")
        print("\tDownload acquired...")    
        browser.close()
     
for id in lsIDs[0:3]:
     main(key=id)

# Merge all card .xlsx to result excel db
xl_path = f"/home/recodera/MRI_dasa/MRI_02/res"
file_list = glob.glob(xl_path + "/*/*.xlsx")
print(file_list)

xl_merged = pd.DataFrame()
for xl_file in file_list:
    xl_red = pd.read_excel(xl_file)
    xl_merged = xl_merged.append(
      xl_red, ignore_index=True)
 
xl_merged.to_excel('res.xlsx', index=False)
print(f'Resulting file written to: {os.getcwd()}')

# Add PK table id to each pdf source folder
# CONTINUE HERE by IF PAR exits then calculate the pdf_tab_id
# file = "/home/recodera/MRI_dasa/MRI_02/Loper/Loper/LosiActa.pdf"
xl_path = "/home/recodera/MRI_dasa/MRI_02/Loper/Loper"

def pdf_tab_id(file):
    from tabula import read_pdf
    from tabulate import tabulate
    import os
    import re
    import json
    import pathlib
    
    fce_path_file = pathlib.Path(file)
    fce_path = fce_path_file.parent
    print(f'fce_path is: {fce_path}')
    ls_df = read_pdf(file, pages="all")
    r = re.compile(r"[01][.]{1}\d{2}")
    ls_id = []
    for count, tb in enumerate(ls_df):
        ls_df[count].to_csv('df_csv.csv')
        with open('df_csv.csv') as f:
            s = f.read()
        dec = re.findall(r, s)
        ls_id.append(dec)
        print(ls_id)

    js_str = json.dumps(ls_id)
    jsonFile = open(f"{fce_path}/id.json", "w")
    jsonFile.write(js_str)
    jsonFile.close()

#pdf_file_list = glob.glob(xl_path + "/*/*PAR.pdf")
pdf_file_list = glob.glob(f'{xl_path}/*/*.pdf')
print(pdf_file_list)
print(xl_path)

for file in pdf_file_list:
    pdf_tab_id(file)