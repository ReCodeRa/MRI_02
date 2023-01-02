import asyncio
from playwright.async_api import async_playwright

key = "DK/H/0241/001"

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://mri.cts-mrp.eu/portal/details?productnumber=DK/H/0241/001")
        download_info = page.expect_download()
        # Perform the action that initiates download
        await page.get_by_text("Download excel").click()
        download = download_info.value()
        # Wait for the download process to complete
        print(await download.path())
        # Save downloaded file somewhere
        download.save_as(f"/{key}/{key}.xlsx")
        
        await browser.close()

asyncio.run(main())