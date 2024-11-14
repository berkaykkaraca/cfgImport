from datetime import datetime
import os
from playwright.sync_api import sync_playwright

def capture_screenshot(url):
    try:
        with sync_playwright() as p:
            print(url)
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(url)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"screenshot_{timestamp}.png"
            screenshot_path = os.path.join('app','static', 'screenshots', filename)
            os.makedirs(os.path.join('app','static', 'screenshots'), exist_ok=True)
            page.wait_for_timeout(5000)
            page.screenshot(path=screenshot_path)
            print(screenshot_path)
            browser.close()
            return filename
    except Exception as e:
        return f"Hata: {str(e)}"