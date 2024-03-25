import json

# Grāmatu krātuve

# Uzraksti programmas kodu, kurš atver, nolasa un pārvērš par strukturētiem datiem teksta datni gramatas.json un saglabā to sarakstā visas_gramatas
with open("gramatas.json", "r", encoding="utf-8") as f:
    dati_raw = f.read()

visas_gramatas = json.loads(dati_raw)

izvele = input("Ko vēlies darīt? pievienot (p) / meklēt (m)")
if izvele == "p":
    gramatas = {}
    autors = input("Grāmatas autors")
    nosaukums = input("Grāmatas nosaukums")
    gads = int(input("Izdošanas gads"))
    lpp = int(input("Lappušu skaits"))
    gramatas["autors"] = autors
    gramatas["nosaukums"] = nosaukums
    gramatas["izdošanas gads"] = gads
    gramatas["lappušu skaits"] = lpp
    visas_gramatas.append(gramatas)
    dati = json.dumps(visas_gramatas, ensure_ascii=False)
    with open("gramatas.json", "w", encoding="utf-8") as f:
        f.write(dati)
elif izvele == "m":
    nosaukums = input("Kādu grāmatas nosaukumu meklēt?")
    for viena_gramata in visas_gramatas:
        if nosaukums in viena_gramata["nosaukums"].lower():
            print(f"Ir atrasta. Pilns nosaukums: {viena_gramata["nosaukums"]}")
        else:
            print("Nav atrasta")

# Izveido teksta ievadi, kas programmas lietotājam ļauj izvēlēties starp divām darbībam – pievienot un meklēt.
# Ja izvēlēta darbība "pievienot", tad programma pieprasa lietotājam šādus datus par grāmatu:
# autors
# nosaukums
# izdošanas gads
# lappušu skaits
# Ievadīto informāciju, izvēloties piemērotus datu tipus, jāievieto vārdnīcā gramatas
# Šo vārdnīcu japievieno sarakstam visas_gramatas
# Saraksta saturu jāieraksta teksta datnē gramatas.json


# Ja izvēlēta darbība "meklēt", tad programma pieprasa lietotājam ievadīt grāmatas nosaukumu vai tā fragmentu un paziņo, vai tāda ir atrodama sarakstā visas_gramatas