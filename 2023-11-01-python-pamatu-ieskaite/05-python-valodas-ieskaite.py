# Par darba veikšanu patstāvīgi 2 punkti. T.i., sēžot atsevišķi, nekonsultējoties ar apkārtējiem.
# Saņemt 10 var vienīgi izpildot šo nosacījumu.


# 1. Izveido teksta mainīgo ar šī mēneša nosaukumu (1 p.)
menesis = "novembris"

# 2. Doti divi skaitliski mainīgie.
# Ar print parādi pirmā mainīgā dalījumu ar otro  (1 p.)
ska1 = 10
ska2 = 11
print(ska1/ska2)

# 3. Izmantojot print ar f-string, kā arī dotos mainīgos, izveido nepieciešamo izteiksmi un izvadi ekrānā teikumu,
# kurš parāda cik dienas atlikušas līdz gada beigām. (2 p.)
novembris = 30
decembris = 31
gads = 2023
print(f"Līdz {2023}. gada beigām atlikušas {novembris+decembris} dienas.")


# 4. Dotajā koda rindā ir kļūda, izlabo! (1 p.)
gads = int(input("Uzraksti, kāds tagad gads!"))


# 5. Maini sk1, sk2 un sk3 vērtības, lai dotā rinda ar print parādītu False (2 p.)
sk1 = 11
sk2 = 1
sk3 = 1
print(sk1 == sk2 or sk1 < sk3)


# 6. Izmanto dotos mainīgos un izveido izteiksmi, kura aprēķina visu preču vērtību centos. 
# Atbildei jābūt jaunam mainīgajam precu_summa (1 p.)
precu_skaits = 2
preces_cena_eur = 3
precu_summa = precu_skaits * preces_cena_eur * 100



# 7. Uzstādi komentāra zīmi visu iepriekšēju koda rindu priekšā. (1 p.)



# 8. Izveido funkciju kapinajums ar vienu parametru, kuram jābūt veselam skaitlim.
# Funkcijai to jāatgriež kāpinātu tādā pašā pakāpē, kā šis skaitlis. (2 p.)
def kapinajums(skaitlis):
    return skaitlis ** skaitlis


# 9. Izveido funkciju divi_skaitli ar diviem skaitliskiem parametriem.
# Ja ja pirmais skaitlis lielāks par otro, tad programma parāda abu skaitļu starpību,
# ja otrais lielāks par pirmo – abu skaitļu summu,
# ja abi vienādi – parāda dubultotu summu. (3 p.)
def divi_skaitli(skaitlis1, skaitlis2):
    if skaitlis1 > skaitlis2:
        print(skaitlis1 - skaitlis2)
    elif skaitlis2 > skaitlis1:
        print(skaitlis1 + skaitlis2)
    else:
        print(2*(skaitlis1 + skaitlis2))


# 10. Izveido funkciju jauna_parole bez parametriem. 
# Funkcijā pieprasa ievadīt divus vārdu vai simbolu virknes.
# Ja tie ievadīti vienādi, tad paziņo "Parole izveidota veiksmīgi." 
# Ja nav vienādi, atkārtoti pieprasa divus vārdus.
# Papildus prasība – ja jebkurš no ievadītajiem vārdiem ir STOP, 
# programma darbu beidz un paziņo "Paroles maiņa atlikta." (4 p.)
def jauna_parole():
    paroles_maina = True
    while paroles_maina:
        parole1 = input("Uzraksti jauno paroli!")
        parole2 = input("Vēlreiz uzraksti jauno paroli!")
        if parole1 == "STOP" or parole2 == "STOP":
            print("Paroles maiņa atlikta.")
            paroles_maina = False
        elif parole1 == parole2:            
            print("Parole izveidota veiksmīgi." )
            paroles_maina = False
        else:
            print("Ievadītās paroles nesakrīt")
        
    

# 11. paskaidro šos operatorus (0.5 p par katru)
# // dalīšana, rezultātam atmetot atlikumu
# == pārbaude, vai divi lielumi ir vienādi
# = piešķir vērtību mainīgajam
# and loģiskais operators. Atgriež True tikai tad, ja abi nosacījumi True

 

# 12. Aizpildi teksta mainīgos labiSapratu un velJapamacas un izlabo skaitlisko mainīgo atzime,
# lai zemāk dotā print rinda parādītu Tavu pašvērtējumu par darbu un paredzamo atzīmi. 
labiSapratu = ""
velJapamacas = ""
atzime = -1

print(f"Manuprāt vislabāk sapratu un izdevās {labiSapratu},\nbet vēl jāuzlabo {velJapamacas}.\nDomāju, ka saņemšu {atzime}.")

# Paldies par darbu!
