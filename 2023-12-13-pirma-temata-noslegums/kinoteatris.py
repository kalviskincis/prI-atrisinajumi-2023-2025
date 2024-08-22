def kino(skaits, laiks):
    if laiks >= 11 and laiks < 18:
        cena = skaits * 4
    elif laiks >= 18 and laiks <= 23:
        cena = skaits * 6
    return cena

iepirkties = True
summa = 0
while iepirkties == True:
    skaits = int(input("Cik biļetes?"))
    laiks = int(input("Cikos?"))
    if laiks >=11 and laiks <=23:
        cena = kino(skaits, laiks)
        print(f"Jāmaksā {cena}.")
        summa += cena
    else:
        print("Kļūda laika izvēlē. Kinoteātris strādā no 11.00 līdz 23.00")

    turpinat = input("Vai turpināt?")
    if turpinat != "J":
        iepirkties = False
print(f"Kopā jāmaksā {summa}.")