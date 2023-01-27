import os
import pandas as pd
from playwright.sync_api import sync_playwright
from itertools import chain 

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
        browser.close()
     
for id in lsIDs[0:9]:
     main(key=id)

import pandas as pd
import glob
from os import getcwd
print(getcwd())
# WRONG!!!
xl_path = "./MRI/res"
file_list = glob.glob(xl_path + "/*/*.xlsx")
print(file_list)

xl_merged = pd.DataFrame()
for xl_file in file_list:
    xl_red = pd.read_excel(xl_file)
    xl_merged = xl_merged.append(
      xl_red, ignore_index=True)
 
xl_merged.to_excel('res.xlsx', index=False)
print(f'Resulting file written to: {getcwd()}')
    