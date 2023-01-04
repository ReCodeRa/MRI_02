import os
from playwright.sync_api import sync_playwright

key = "2731"
os.makedirs(f"res/{key}", exist_ok=True)

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://mri.cts-mrp.eu/portal/details?productnumber=NL/H/2731/001")
        
        with page.expect_download() as download_info:
            page.get_by_text("Download excel").click()
        download = download_info.value
        download.save_as(f"res/{key}/{key}.xlsx")    
       
        # Selector for document download buttons: .mat-button-base.ng-star-inserted
       
        browser.close()
main()