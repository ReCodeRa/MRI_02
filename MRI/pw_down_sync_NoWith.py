from playwright.sync_api import sync_playwright

key = "0107"

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://mri.cts-mrp.eu/portal/details?productnumber=LT/H/0107/001")
        #page.goto("https://mri.cts-mrp.eu/portal/details?productnumber=NL/H/2664/001", wait_until='networkidle')

        with page.expect_download() as download_info:
            page.get_by_text("Download excel").click(timeout=2000)
        download = download_info.value
        # wait for download to complete
        path = download.path()
        print(path)
        # Save downloaded file somewhere
        download.save_as(f"{key}.xlsx")    
        browser.close()
main()