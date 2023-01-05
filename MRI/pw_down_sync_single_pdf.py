import os
from playwright.sync_api import sync_playwright

key = "2731"
os.makedirs(f"res/{key}", exist_ok=True)

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo= 5000)
        page = browser.new_page()
        page.goto("https://mri.cts-mrp.eu/portal/details?productnumber=NL/H/2731/001", wait_until="networkidle")
        
        # with page.expect_download() as download_info:
        #     page.get_by_text("Download excel").click()
        # download = download_info.value
        # download.save_as(f"res/{key}/{key}.xlsx")    
       
        # Selector for document download buttons: .mat-button-base.ng-star-inserted
        # STUDY LOCATOR METHODS, esp. "nth" in iterator
        elements = page.get_by_role("listitem").get_by_role("button").all()
        count = elements.count()
        print(f"Number of detected elements is: {count}")
        for doc in elements:
        

        # for i in range(count):
        #     elements.nth(i).click(modifiers=["Control", "Shift"])

        # handles = page.query_selector_all(".documents-list .mat-button-wrapper .mat-icon-no-color")

            with page.expect_download() as download_info:
                doc.click()
            download = download_info.value
            doc_name = download.suggested_filename
            download.save_as(f"res/{key}/{doc_name}.pdf")
    
        browser.close()
main()