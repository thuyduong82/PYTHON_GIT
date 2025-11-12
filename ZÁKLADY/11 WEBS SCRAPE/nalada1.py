from bs4 import BeautifulSoup 
import requests 
def main():
    url = "https://www.arsenal.com/results" 
    response = requests.get(url) 
    soup = BeautifulSoup(response.content, "html.parser") 
    

    all_scores = soup.select("span.scores__score") 
    arsenal_score = soup.select_one("span.scores__score--arsenal") 

    who = soup.select_one("div.team-crest__name-value")
     

    arsenal = int(arsenal_score.text.strip())
    for s in all_scores:
        if s != arsenal_score:
            team2 = int(s.text.strip())
            break # rozhodnutí 
    

    if arsenal > team2: print("Učitel je super šťastný.")
    elif arsenal < team2: print("Učitel se velmi zlobí a nemá dobrou náladu.") 
    else: print("Učitel má smíšené emoce bo to byla remíza") 

    print(who.text)
    if who.text == "Sunderland":
        print("ucitel je super 10krát nastvanější")

if __name__ == "__main__":
    main()