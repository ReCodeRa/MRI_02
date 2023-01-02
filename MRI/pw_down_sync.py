from playwright.sync_api import sync_playwright

key = "DK/H/0241/001"

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://mri.cts-mrp.eu/portal/details?productnumber=DK/H/0241/001")
        download_info = page.expect_download()
        # Perform the action that initiates download
        page.get_by_text("Download excel").click()
    download = download_info.value()
        # Wait for the download process to complete
    print(download.path())
        # Save downloaded file somewhere
    download.save_as(f"/{key}/{key}.xlsx")
        
    browser.close()

main()