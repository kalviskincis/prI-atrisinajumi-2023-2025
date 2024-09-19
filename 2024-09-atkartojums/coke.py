nominali = [5, 10, 25]
atlicis = 50
while atlicis > 0:
    print(f"Amount Due: {atlicis}")
    nonemt = int(input("Insert Coin: "))
    if nonemt in nominali: 
        atlicis -= nonemt
print(f"Change Owed: {atlicis*-1}")