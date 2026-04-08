hokus = (50,100,150)

for x in hokus:
    print(x)

print(hokus[1])

names =["eva","jana","adela","bara","sara"]
names.append("klara")
print(names[2])

for i, name in enumerate(names):#enumarate rika pridat si cislo, i index
    print(f"{i+1}. {name}")

names.pop(1)
print(names[-1])

ukazka = {
    "matika":"2",
    "cestina":"1",
    "fyzika":"3"
}
for key in ukazka:
    print(f"(key)")

for key in ukazka:#vypise pravou cast value
    print(ukazka[key])#1.kolo cat["name"] 2.kolo cat["age"]