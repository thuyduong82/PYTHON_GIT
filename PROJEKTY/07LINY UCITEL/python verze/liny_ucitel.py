import random, json, os 

path = "znaky.json"

studenti = {
    "Adam": "",
    "Bar": "",
    "Cyril": "",
    "Denisa": "",
    "Eva": ""
}

def ulozeni():
    with open(path, mode="w") as file:
        json.dump(studenti, file, indent=2)
print("ulozene")



def udel_znamku(jmeno):
    if jmeno in studenti:
        znamka = str(random.randint(1, 5))
        studenti[jmeno] = znamka
        print(f"Student {jmeno} dostal známku {znamka}.")
    else:
        print(f"Student {jmeno} není v seznamu.")
    ulozeni()

jmeno = input("Zadej jméno studenta: ")
udel_znamku(jmeno)


