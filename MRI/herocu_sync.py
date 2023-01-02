from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/download", wait_until='networkidle')

    with page.expect_download() as download_info:
        page.get_by_text("Excel.xlsx").click()
    download = download_info.value
    # wait for download to complete
    path = download.path()
    print(path)
    # Save downloaded file somewhere
    download.save_as(f"/{key}/{key}.xlsx")
        
    browser.close()

main()