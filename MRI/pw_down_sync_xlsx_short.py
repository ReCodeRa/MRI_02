import os
import pandas as pd
from playwright.sync_api import sync_playwright
from itertools import chain 

# Read IDs from .csv to ls
df = pd.read_csv('lsIDs.csv', delimiter=',')
lsls = [list(row) for row in df.values]
lsIDs = list(chain.from_iterable(lsls))
print(lsIDs[0:3])
  
# printing the data
print(data_into_list)
my_file.close()


# key = "5163"
os.makedirs(key, exist_ok=True)

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://mri.cts-mrp.eu/portal/details?productnumber=NL/H/5163/001")
        
        with page.expect_download() as download_info:
            page.get_by_text("Download excel").click()
        download = download_info.value
        download.save_as(f"{key}/{key}.xlsx")    
        browser.close()
main()