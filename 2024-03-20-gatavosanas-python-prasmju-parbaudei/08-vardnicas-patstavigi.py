# Izveido vārdnīcu vai vārdnīcas situācijas aprakstam
# (šajā uzdevumā nav jādemonstrē vārdnīcu metožu pārzināšana, bet gan plānošana)

# Maza picērija piedāvā diva veida picas – siera un desas.
# Abiem veidiem pieejami 3 izmēri: 20, 30 un 45 cm
# Cena katram no izmēriem, neatkarīgi no picas veida ir 7.50, 12.50 un 17.50 EUR

picas1 = {
        "veidi": ["siera", "desas"],
        "cenas": {"20": 7.50, "30": 12.50, "45": 17.50}
}

picas2 = [
    {
        "veids": "siera",
        "izmeri": ["20", "30", "45"],
        "cenas": [7.50, 12.50, 17.50]
     },
    {
        "veids": "desas",
        "izmeri": ["20", "30", "45"],
        "cenas": [7.50, 12.50, 17.50]
    }
]

# Dota vārdnīca
modinatajs = {"pirmdiena": "6.00", "otrdiena": "6:00", "trešdiena": "5:45", "ceturtdiena": "6:00", "piektdiena": "7:00", "sestdiena": "7:00", "svētdiena": "9:00"}
# Maini atslēgas "sestdiena" vērtību uz "9:00"
modinatajs["sestdiena"] = "9:00"
# Parādi atslēgu-vērtību pārus stabiņā uz leju
for diena, laiks in modinatajs.items():
    print(diena, laiks)


# Dota vārdnīca
sokolade = {"Nosaukums": "Sarkanā magone", "Svars": 90, "Cena": 2.29}
# Parādi atslēgu "Nosaukums" un "Cena" vērtības
print(sokolade["Nosaukums"])
print(sokolade["Cena"])



# Dota vārdnīca
dati_vienk = {
        "status": {
            "verified": True,
            "sentCount": 1
        },
        "type": "cat",
        "deleted": False,
        "_id": "5a4d776e6ef087002174c291",
        "updatedAt": "2020-08-23T20:20:01.611Z",
        "createdAt": "2018-07-09T20:20:03.328Z",
        "user": "5a9ac18c7478810ea6c06381",
        "text": "The claws on the cat’s back paws aren’t as sharp as the claws on the front paws because the claws in the back don’t retract and, consequently, become worn.",
        "source": "user",
        "__v": 0,
        "used": False
    }
# Parādi atslēgas "text" vērtību
print(dati_vienk["text"])

# Dota datu struktūra
dati_salikt = [{"status": {"verified": None, "sentCount": 0}, "type": "cat", "deleted": False, "_id": "5fd56cdcb3fb8b0017357170", "user": "5fd56c8db3fb8b0017357163", "text": "Cats\u2019 collarbones don\u2019t connect to their other bones, as these bones are buried in their shoulder muscles.", "createdAt": "2020-12-13T01:22:36.794Z", "updatedAt": "2020-12-13T01:22:36.794Z", "__v": 0}, {"status": {"verified": None, "sentCount": 0}, "type": "cat", "deleted": False, "_id": "6054cb43db0a6f0017161b83", "user": "6054ca91db0a6f0017161b34", "text": "Catsssss0.44187486742960624.", "createdAt": "2021-03-19T16:03:15.135Z", "updatedAt": "2021-03-19T16:03:15.135Z", "__v": 0}, {"status": {"verified": True, "sentCount": 1}, "type": "cat", "deleted": False, "_id": "5a4d776e6ef087002174c291", "updatedAt": "2020-08-23T20:20:01.611Z", "createdAt": "2018-07-09T20:20:03.328Z", "user": "5a9ac18c7478810ea6c06381",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         "text": "The claws on the cat\u2019s back paws aren\u2019t as sharp as the claws on the front paws because the claws in the back don\u2019t retract and, consequently, become worn.", "source": "user", "__v": 0, "used": False}, {"status": {"verified": True, "sentCount": 1}, "type": "cat", "deleted": False, "_id": "591f98803b90f7150a19c226", "__v": 0, "text": "The cat's footpads absorb the shocks of the landing when the cat jumps.", "source": "api", "updatedAt": "2020-08-23T20:20:01.611Z", "createdAt": "2018-01-04T01:10:54.673Z", "used": False, "user": "5a9ac18c7478810ea6c06381"}, {"status": {"verified": True, "sentCount": 1}, "type": "cat", "deleted": False, "_id": "59a60b996acf530020f35870", "updatedAt": "2020-08-23T20:20:01.611Z", "createdAt": "2018-04-06T20:20:05.809Z", "user": "5a9ac18c7478810ea6c06381", "text": "\"Cat people\" are 11% more likely to be introverted than others.", "source": "user", "__v": 0, "used": False}]

# Ar piemērotu funkciju noskaidro, cik ieraksti ir dotajā datu struktūrā
print(len(dati_salikt))

# Parādi visu atslēgu "text" vērtības
for katrs in dati_salikt:
    print(katrs["text"])
