from playwright.sync_api import sync_playwright #synchroni kód=> znamená řádek po řádku postupně
from dotenv import load_dotenv
from os import getenv

load_dotenv()

login = getenv("LOGIN")
password = getenv("PASSWORD")

def main():
    
    with sync_playwright() as p: #otevirame knihovnu a ukladame pod p
        browser = p.chromium.launch(headless=False)#otvirame prohlizec, headles false znamená že se prohlizec ukaze co dela
        page = browser.new_page()#otvírá nový tab

        page.goto("https://www.moodle-trebesin.cz")#stránka jde na url

        page.click('span.login.pl-2')#kdyz kliknu na span s class login a pl2 prihlasi me to 

        page.fill('input#username', login )#vlozi do username nguyen

        page.fill('input#password', password)

        page.click('button#loginbtn')#prihlasi se to

        input("zmáčni jakoukoli klávesu pro zavření prohlížeče")

        browser.close()#uzavře prohlížeč


if __name__== "__main__":
    main()