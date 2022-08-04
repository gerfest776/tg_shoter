import asyncio
from datetime import datetime

from pyppeteer import launch

from utils.whois import get_whois


class Screener:
    def __init__(self, url: str):
        self.url = url

    async def screen_page(self):
        browser = await launch({"args": ["--no-sandbox"]})
        page = await browser.newPage()
        await page.setViewport({"width": 1280, "height": 1280, "deviceScaleFactor": 0})
        await page.goto(self.url)
        path = f"./media/temp/{datetime.now()}.png"
        await asyncio.sleep(1)
        await page.screenshot(
            {
                "path": path,
            }
        )
        await get_whois(self.url)
        await browser.close()
        return path
