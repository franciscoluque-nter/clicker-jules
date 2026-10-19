import os
import time
import http.server
import socketserver
import threading
from playwright.sync_api import sync_playwright

PORT = 8085

def start_server():
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        httpd.serve_forever()

def run_tests():
    # Start background HTTP server
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()
    time.sleep(1) # wait for server to start

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        url = f"http://localhost:{PORT}/index.html"
        page.goto(url)

        cookie_btn = page.locator("#cookie-btn")
        click_count = page.locator("#click-count")
        reset_btn = page.locator("#reset-btn")

        trophy_10 = page.locator("#trophy-10")
        trophy_100 = page.locator("#trophy-100")
        trophy_1000 = page.locator("#trophy-1000")

        status_10 = page.locator("#status-10")
        status_100 = page.locator("#status-100")
        status_1000 = page.locator("#status-1000")

        # Initial check
        assert click_count.text_content() == "0"
        assert "unlocked" not in (trophy_10.get_attribute("class") or "")

        # Click 10 times to unlock Bronze Cookie
        for i in range(10):
            cookie_btn.click()

        assert click_count.text_content() == "10"
        assert "unlocked" in (trophy_10.get_attribute("class") or "")
        assert "Unlocked" in status_10.text_content()
        print("Bronze trophy (10 clicks) verified!")

        # Set cookie directly to 100 and reload page to verify persistence & Silver unlock
        context.add_cookies([{
            "name": "cookieClickCount",
            "value": "100",
            "url": url
        }])
        page.reload()

        assert click_count.text_content() == "100"
        assert "unlocked" in (trophy_100.get_attribute("class") or "")
        assert "Unlocked" in status_100.text_content()
        print("Silver trophy (100 clicks) & cookie persistence verified!")

        # Set cookie directly to 1000 and reload page to verify Gold unlock
        context.add_cookies([{
            "name": "cookieClickCount",
            "value": "1000",
            "url": url
        }])
        page.reload()

        assert click_count.text_content() == "1000"
        assert "unlocked" in (trophy_1000.get_attribute("class") or "")
        assert "Unlocked" in status_1000.text_content()
        print("Gold trophy (1000 clicks) verified!")

        # Verify DevTools restrictions
        contextmenu_prevented = page.evaluate("""() => {
            const event = new MouseEvent('contextmenu', { bubbles: true, cancelable: true });
            return !document.dispatchEvent(event);
        }""")
        assert contextmenu_prevented == True
        print("Context menu default prevented: True")

        f12_prevented = page.evaluate("""() => {
            const event = new KeyboardEvent('keydown', { key: 'F12', bubbles: true, cancelable: true });
            return !document.dispatchEvent(event);
        }""")
        assert f12_prevented == True
        print("F12 key default prevented: True")

        # Test reset button
        reset_btn.click()
        assert click_count.text_content() == "0"
        assert "unlocked" not in (trophy_10.get_attribute("class") or "")
        assert "unlocked" not in (trophy_100.get_attribute("class") or "")
        assert "unlocked" not in (trophy_1000.get_attribute("class") or "")
        print("Reset functionality verified!")

        # Trigger 10 clicks again for visual verification screenshot
        for i in range(10):
            cookie_btn.click()

        screenshot_path = os.path.abspath("verification/verification_achievements.png")
        page.screenshot(path=screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    run_tests()
