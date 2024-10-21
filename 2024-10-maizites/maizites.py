import sys

def main():
    vards = input("Kā Tevi sauc?")
    cena = input("Cik maksā viena maizīte?")
    skaits = input("Cik maizītes pirksi?")
    try:
        cena_f = float(cena)
        skaits_i = int(skaits)
        if cena_f > 0 and skaits_i > 0 and len(vards) > 0:
            summa = aprekins(cena_f, skaits_i)
            vards_lielie = varda_formatesana(vards)
            print(f"Klients {vards_lielie}")
            print(f"Kopā jāmaksā {summa}.")
        else:
            print("Nepareizi dati.")
            sys.exit()
    except:
        print("Nepareizi dati.")
    

def aprekins(cena, skaits):
    summa = cena*skaits
    return summa

def varda_formatesana(vards):
    vards_lielie = vards.upper()
    return vards_lielie

if __name__ == "__main__":
    main()