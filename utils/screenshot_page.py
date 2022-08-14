import asyncio
from datetime import date

from loguru import logger
from pyppeteer import launch

from utils.whois import get_whois


def url_to_filename(url: str):
    return url.split("//")[1].split(".")[0]


class Screener:
    def __init__(self, url: str, user_id: int):
        self.url = url
        self.user_id = user_id

    async def screen_page(self):
        """
        Making screenshots with 1s sleep to fully load bit sites
        :return:
        """
        logger.info(f"Start screen url page {self.url}")
        browser = await launch(
            executablePath="/usr/bin/google-chrome-stable",
            headless=True,
            args=["--no-sandbox"],
        )
        page = await browser.newPage()
        await page.setViewport({"width": 1280, "height": 1280, "deviceScaleFactor": 0})
        await page.goto(self.url)
        path = f"./media/temp/{date.today()}-{self.user_id}-{url_to_filename(self.url)}.png"
        await asyncio.sleep(1)
        try:
            await page.screenshot(
                {
                    "path": path,
                }
            )
        except Exception as e:
            logger.error(f"Error when trying screenshot {e}")
        await get_whois(self.url)
        await browser.close()
        return path
