import json
def uzd1():
    ## Atpazīsti! (2 p.)
    # Izdzēs visas rindas, kurās mainīgo vērtība nav vai nesatur vārdnīcas
    saldejumi4 = {"Nosaukums": "Rūjienas", "Garša": "Šokolādes"}
    saldejumi6 = [{"Nosaukums": "Rūjienas"}, {"Nosaukums": "Karlsons"}, {"Nosaukums": "Pols"}]
    saldejumi8 = {1: "Pols", 2: "Karlsons", 3: "Rūjienas", 4: "Tio"}


def uzd2():
    ## Papildini, maini, parādi! (6 p.)
    # Dota vārdnīca
    plaukts = {"Nosaukums": "Kallax", "platums": 0.77, "augstums": 0.77}

    # pievieno tai jaunu atslēgu "krāsa" ar vērtību "balta"
    # pievieno tai jaunu atslēgu "cena" ar skaitlisku vērtību 39.99
    plaukts["krāsa"] = "balta"
    plaukts["cena"] = 39.99

    # Uzraksti kodu, kurš parāda visas vērtības vienā rindā
    print(plaukts.values())
    # Maini atslēgas "krāsa" vērtību uz "melna"
    plaukts["krāsa"] = "melna"

    # Parādi visas atslēgas kopā ar vērtībām (vienalga, vai stabiņā uz leju vai vienā rindā)
    for atslega in plaukts:
        print(f"{atslega}, {plaukts[atslega]}")

    # Izveido vārdnīcu "galds" ar tādam pat atslēgām kā šai plaukta vārdnīcai (tajā skaitā jaunās atslēgas "krāsa" un "cena"), vērtības var izdomāt vai atrast kādā mēbeļu veikalā.
    # Abas vārdnīcas pievieno sarakstam "mebeles", to vispirms izveidojot tukšu.
    galds = {"Nosaukums": "Compact", "platums": 1, "augstums": 0.80, "krāsa": "kļava", "cena": "75"}
    mebeles = []
    mebeles.append(plaukts)
    mebeles.append(galds)


def uzd3():
    ## Plāno un veido! (4 p.)
    # Izdomā kādu personu (piemēram, filmu vai spēļu varoni), priekšmetu, augu, procesu (piemēram, biļešu iegādi, ēdiena pasūtīšana ar piegādi) vai ko citu un tam piemērotas īpašības.
    # Izveido vārdnīcu ar 3 līdz 4 atslēgu-vērtību pāriem Tevis izdomātajam.
    # Šo vārdnīcu ieraksti JSON datnē "mans.json"
    limuzins = {"krāsa": "Jāņu nakts krāsā", "izlaiduma gads": 1981, "īpašnieks": "Mirta Saknīte"}
    dati = json.dumps(limuzins, ensure_ascii=False)
    with open("mans.json", "w", encoding="utf-8") as f:
        f.write(dati)

def uzd4():
    ## Nolasi un parādi! (4 p.)s
    # atver un nolasi JSON dati zinatnieki.json
    # parādi tās saturu ekrānā (bez kādas sevišķas izkārtošanas, vienkārši ar print).
    # Papilduzdevums – parādi saturu ekrānā glītak izkārtotu.
    with open("zinatnieki.json", "r", encoding="utf-8") as datne:
        dati = datne.read()

    zinatnieki = json.loads(dati)

    print(zinatnieki)

    for viens_zinatnieks in zinatnieki:
        for atslega in viens_zinatnieks:
            print(f"{atslega} - {viens_zinatnieks[atslega]}")
        print()
# uzd1()
# uzd2()
# uzd3()
# uzd4()