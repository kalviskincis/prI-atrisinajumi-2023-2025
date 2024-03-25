# Izveido sarakstu ar diviem skaitliskiem ierakstiem
divi_skaitli = [0, 1]

# Dots saraksts
kabineti = ["401", "402", "404"]
# Ar piemērotu metodi pievieno ierakstu "403", lai tas atrastos secībā pareizā vietā
kabineti.insert(2, "403")

# Doti divi saraksti
sakums = ["ziema", "pavasaris"]
beigas = ["rudens", "ziema"]
# Ar piemērotu metodi apvieno abus sarakstus vienā ar nosaukumu "gads"
gads = sakums + beigas

# Dots saraksts
temperaturas = [7.2, 6.7, 6.8, 7.0]
# Paredzēts, ka katru temperatūru parāda vienu zem otras, bet tas nestrādā. Izlabo!
for viena in temperaturas:
    print(viena)


# Dots saraksts
cenas = [1.667, 1.667, 1.607, 1.597]
# Ar piemērotām metodēm izdzēs pirmo un pēdējo saraksta ierakstus
cenas.pop()
cenas.pop(0)
