from playwright.sync_api import sync_playwright
from pathlib import Path
import os

key = "4900"
os.makedirs(f"res/{key}", exist_ok=True)

path = Path().home() / 'Downloads'
timeout = 30 * 1000                  #  timeout

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://mri.cts-mrp.eu/portal/details?productnumber=NL/H/4900/001", timeout=timeout)
        
        
        with page.expect_download() as download_info:
            page.get_by_text("Download excel").click()
        download = download_info.value
        download.save_as(f"res/{key}/{key}.xlsx") 
        
        page.wait_for_selector('mat-card', timeout=timeout) # completely load the page
        downloads = page.locator('mat-card').locator("button")
        # texts = await downloads.all_text_contents() # just making sure I got what I thought I got
        count = downloads.count()
        print(f'There are {count} buttons in mat-card section.')

# Starting here is where I can't follow the API

        for i in range(count):
            print(f"Starting download {i}")
            with page.expect_download() as download_handler:
                downloads.nth(i).click(timeout=0)
            download = download_handler.value
            doc_name = download.suggested_filename
            download.save_as(f"res/{key}/{doc_name}")
    
    print("\tDownload acquired...")
    browser.close()
main()