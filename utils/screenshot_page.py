from datetime import datetime
from pyppeteer import launch


class Screener:
    def __init__(self, url: str):
        self.url = url

    async def screen_page(self):
        browser = await launch()
        page = await browser.newPage()
        await page.setViewport({'width': 1920, 'height': 1080, "deviceScaleFactor": 0})
        await page.goto(self.url)
        path = f'./media/temp/{datetime.now()}.png'
        await page.screenshot(
            {
                'path': path,
                'fullPage': True
            }
        )
        await browser.close()
        return path


