from playwright.sync_api import sync_playwright

key = "NL/H/2664/001"

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://mri.cts-mrp.eu/portal/details?productnumber=NL/H/2664/001")
    with page.expect_download() as download_info:
        page.get_by_text("Download file").click()
    download = download_info.value
    # wait for download to complete
    path = download.path()
    print(path)
    # Save downloaded file somewhere
    download.save_as(f"/{key}/{key}.xlsx")
        
    browser.close()

main()