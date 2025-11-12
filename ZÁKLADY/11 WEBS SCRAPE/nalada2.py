from bs4 import BeautifulSoup
import requests

def main():
    url = "https://www.arsenal.com/results"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    nearsenal = soup.find_all("span", class_="scores__score")[0]

    for score in nearsenal:
        print(score.text)

    arsenal = soup.find_all("span", class_="scores__score scores__score--arsenal")

    for ascore in arsenal:
        print(ascore.text)

    team = soup.find_all("div", class_="team-crest__name-value")
    for name in team:
        print(name.text)


    if ascore > score:
        print("YEEEEE, velmi dobra nalada")
    if ascore < score:
        print("NEEEEEEE")
    if ascore == score:
        print(":/")
    if name == "Sunderland":
        print("nalada x10")




if __name__ == "__main__":
    main()
