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
    os.makedirs(id_uds, exist_ok=True)
   
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(f"https://mri.cts-mrp.eu/portal/details?productnumber={key}")
        
        with page.expect_download() as download_info:
            page.get_by_text("Download excel").click()
        download = download_info.value
        download.save_as(f"{key}/{key}.xlsx")    
        browser.close()
    
  
# printing the data
print(data_into_list)
my_file.close()
for id in lsIDs:
     main(key=id)


    