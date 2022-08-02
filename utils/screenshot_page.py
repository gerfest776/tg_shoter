from datetime import datetime
from pyppeteer import launch


class Screener:
    def __init__(self, url: str):
        self.url = url

    async def screen_page(self):
        browser = await launch({'args': ['--no-sandbox']})
        page = await browser.newPage()
        await page.setViewport({'width': 1080, 'height': 1920, "deviceScaleFactor": 1})
        await page.goto(self.url)
        path = f'./media/temp/{datetime.now()}.png'
        await page.screenshot(
            {
                'path': path,
            }
        )
        await browser.close()
        return path


