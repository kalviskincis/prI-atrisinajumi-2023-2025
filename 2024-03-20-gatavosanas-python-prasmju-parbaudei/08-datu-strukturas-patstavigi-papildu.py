# Dota datne laureate.json, kurā ir dati par daļu Nobela miera prēmijas laureātu
# Iepazīsties ar JSON datnes laureate.json struktūru
# Izdomā, kādus datus, kurus no šīs datu kopas vēlies parādīt un izveido programmu, kura to paveic.

# Piemēram, visu laureātu vārdi, uzvārdi, joma, kurā pasniegta balva un konkrētais iemesls.
# Vai visi fiziķi, visi francūži vai visi balvu saņēmēji, kuri dzimuši 19. gadsimtā -- Tava vaļa idejām.
import json

with open("laureate.json", "r", encoding="utf-8") as datne:
    dati_raw = datne.read()
dati = json.loads(dati_raw)

visi = dati["laureates"]
for katrs in visi:
    vards = katrs["firstname"]
    try:
        uzvards = katrs["surname"]
    except KeyError:
        uzvards = ""
    par_ko = ""
    for viens in katrs["prizes"]:
        gads = viens["year"]
        par_ko += f"{viens["motivation"]} {"\n"} "
    print(f"{vards}, {uzvards}, {gads}, {par_ko}")
