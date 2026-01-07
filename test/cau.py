from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
from os import getenv

load_dotenv()

login = getenv("LOGIN")
password = getenv("PASSWORD")

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("")
        page.click('')
        page.fill('',password)

        input("zmackni klaseu")
        browser.close()

if __name__=="__main__":
    main()