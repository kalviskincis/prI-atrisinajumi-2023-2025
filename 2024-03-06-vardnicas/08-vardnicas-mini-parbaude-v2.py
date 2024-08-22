import json


def uzd1():
    ## Atpazīsti! (2 p.)
    # Izdzēs visas rindas, kurās mainīgo vērtība nav vai nesatur vārdnīcas

    saldejumi2 = {1: "Pols", 2: "Karlsons", 3: "Rūjienas", 4: "Tio"}
    saldejumi4 = {"Nosaukums": "Rūjienas", "Garša": "Šokolādes"}
    saldejumi6 = [{"Nosaukums": "Rūjienas"}, {"Nosaukums": "Karlsons"}, {"Nosaukums": "Pols"}]


def uzd2():
    ## Papildini, maini, parādi! (6 p.)
    # Dota vārdnīca
    plaukts = {"Nosaukums": "Billy", "platums": 0.80, "augstums": 2.37}

    # pievieno tai jaunu atslēgu "krāsa" ar vērtību "balta"
    # pievieno tai jaunu atslēgu "cena" ar skaitlisku vērtību 76

    # Uzraksti kodu, kurš parāda visas atslēgas vienā rindā

    # Maini atslēgas "krāsa" vērtību uz "brūna"

    # Parādi visas atslēgas kopā ar vērtībām (vienalga, vai stabiņā uz leju vai vienā rindā)

    # Izveido vārdnīcu "pakaramais" ar tādam pat atslēgām kā šai plaukta vārdnīcai (tajā skaitā jaunās atslēgas "krāsa" un "cena"), vērtības var izdomāt vai atrast kādā mēbeļu veikalā.
    # Abas vārdnīcas pievieno sarakstam "mebeles", to vispirms izveidojot tukšu.
    pakaramais = {}
    mebeles = []
    mebeles.append(pakaramais)
    mebeles.append(plaukts)



def uzd3():
    ## Plāno un veido! (4 p.)
    # Izdomā kādu personu, priekšmetu, augu, procesu vai ko citu un tam piemērotas īpašības.
    # Izveido vārdnīcu ar 3 līdz 4 atslēgu-vērtību pāriem Tevis izdomātajam.
    # Šo vārdnīcu ieraksti JSON datnē "programmesana.json"
    pass # kad sāc darbu, šo rindu noņem

def uzd4():
    ## Nolasi un parādi! (4 p.)s
    # Sastādi programmas kodu, kurš atver un nolasa JSON dati bankomats.json
    # parādi tās saturu ekrānā (bez kādas sevišķas izkārtošanas, vienkārši ar print).
    # izpēti datu struktūru un parādi saturu ekrānā glītak izkārtotu.
    with open("bankomats.json", "r", encoding="utf-8") as f:
        dati = f.read()

    dati_v = json.loads(dati)
    print(dati_v)
    for viens in dati_v:
        print(viens)

uzd1()
# uzd2()
# uzd3()
uzd4()