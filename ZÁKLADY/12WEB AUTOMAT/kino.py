from playwright.sync_api import sync_playwright #synchroni kód=> znamená řádek po řádku postupně
from dotenv import load_dotenv
from os import getenv 
import json

load_dotenv()

path = "data.json"


def main():
    
    with sync_playwright() as p: #otevirame knihovnu a ukladame pod p
        browser = p.chromium.launch(headless=False)#otvirame prohlizec, headles false znamená že se prohlizec ukaze co dela
        page = browser.new_page()#otvírá nový tab


        page.goto("https://www.kinoaero.cz/?sort=sort-by-data")#stránka jde na url

        page.goto("https://www.kinoaero.cz/?sort=sort-by-data&projection=43158")

        movies = page.locator('h3').nth(0).inner_text()
        price = float(page.locator('span').nth(0).inner_text())

        page.goto("https://www.csfd.cz/")

        search_box = page.wait_for_selector("input.tt-input")

        search_box.click()
        search_box.fill(movies)
        search_box.press("Enter")

        page.click('a.film-title-name')

        rating = int(
            page.locator("div.film-rating-average").first.inner_text() # Získá text hodnocení
            .replace("%", "")                                           # Odstraní "%"
        )

        print("hodnocení filmu je:", rating)
        data = {
            "movie_name": movies,
            "rating": rating
        }

        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        print("Uloženo do:", path)

        def vyplati_se(ratingofc, price):
            return(ratingofc/price)
        
        vyplati_se()
        

        input("zmáčni jakoukoli klávesu pro zavření prohlížeče")


        browser.close()#uzavře prohlížeč


if __name__== "__main__":
    main()