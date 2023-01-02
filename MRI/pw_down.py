import asyncio
from playwright.async_api import async_playwright

key = "DK/H/0241/001"

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("http://playwright.dev")
        print(await page.title())
        await browser.close()

asyncio.run(main())

# Start waiting for the download
async def down():
    async with page.expect_download() as download_info:
    # Perform the action that initiates download
        await page.get_by_text("Download file").click()
    download = await download_info.value
    # Wait for the download process to complete
    print(await download.path())
    # Save downloaded file somewhere
    download.save_as("/path/to/save/download/at.txt")