from playwright.sync_api import sync_playwright 
from dotenv import load_dotenv
from os import getenv 
import json

load_dotenv()
path = "data2.json"

# Funkce pro Výpočet (pracuje s desetinnými čísly)
def vyplati_se(rating_value, price_value):
    """Vypočítá poměr hodnocení (0-100) a ceny."""
    if price_value == 0:
        print("Chyba: Cena je 0, nelze dělit.")
        return 0.0
    return rating_value / price_value

# -------------------------------------------------------------
# --- Hlavní Funkce ---
# -------------------------------------------------------------
def main():
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Jdeme na stránku Kina Aero
        page.goto("https://www.kinoaero.cz/?sort=sort-by-data&projection=43158")

        movies = page.locator('h3').nth(0).inner_text()
        
        # --- OPRAVENÝ SELEKTOR PRO CENU A PŘEVOD NA FLOAT ---
        # Hledáme span, který je uvnitř bloku s promítáním (za názvem H3).
        # Třída '.col-xs-12' je typická pro bloky. Toto je opravený odhad selektoru.
        try:
            price_text = page.locator('span').inner_text()
            price_float = float(
                price_text
                .replace("Kč", "")                       
                .replace(" ", "")
                .replace(",", ".") # Převedeme čárku na tečku
            )
        except Exception as e:
            # Pokud se selektor netrefí, nastavíme cenu na 0, aby kód nespadl
            print(f"Varování: Nepodařilo se získat cenu. Použita cena 0. Chyba: {e}")
            price_float = 0.0
        
        # 2. Jdeme na ČSFD
        page.goto("https://www.csfd.cz/")
        search_box = page.wait_for_selector("input.tt-input")
        search_box.click()
        search_box.fill(movies)
        search_box.press("Enter")
        page.click('a.film-title-name')

        # --- ZÍSKÁNÍ A ČIŠTĚNÍ HODNOCENÍ NA FLOAT ---
        # Získáme text (např. "85%"), odstraníme "%" a převedeme na float.
        rating_float = float(
            page.locator("div.film-rating-average").first.inner_text()
            .replace("%", "")
        )
            
        
        print(f"Film: {movies}")
        print(f"Hodnocení (float): {rating_float}%")
        print(f"Cena (Kč): {price_float}")
        
        # 3. Provedeme výpočet
        value_ratio = vyplati_se(rating_float, price_float) 
        
        print(f"Poměr Hodnocení/Cena (Value Ratio): {value_ratio:.4f}")
        
        # 4. Uložení
        data = {
            "movie_name": movies,
            "rating_float": rating_float,
            "price_float": price_float,
            "value_ratio": f"{value_ratio:.4f}"
        }

        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        print(f"Uloženo do: {path}")

        input("Stiskni ENTER pro zavření prohlížeče")

        browser.close()


if __name__== "__main__":
    main()