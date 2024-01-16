def programma():
    sakuma_pop = iegut_skaitu("Ievadiet sākotnējo populāciju (vismaz 9): ", 9)
    beigu_pop = iegut_skaitu(f"Ievadiet beigu populāciju (vismaz {sakuma_pop}): ", sakuma_pop)
    gadu_skaits = aprekinat_dienas(sakuma_pop, beigu_pop)
    print(f"Dienas: {gadu_skaits}")

def iegut_skaitu(teksts, mazaka_robeza):
    while True:
        pop_izmers = int(input(teksts))
        if pop_izmers >= mazaka_robeza:
            break
    return pop_izmers

def aprekinat_dienas(sakuma_pop, beigu_pop):
    dienas = 0
    while sakuma_pop < beigu_pop:
        sakuma_pop += (sakuma_pop // 3) - (sakuma_pop // 4)
        dienas += 1
    return dienas

programma()