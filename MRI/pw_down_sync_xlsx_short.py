import os
from playwright.sync_api import sync_playwright

text = "NO/H/0279/003"
sp = text.split('/')
key = sp[2]


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