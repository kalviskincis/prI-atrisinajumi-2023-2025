menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def noteikt_vertibu(pasutijums):
    try:
        vertiba = menu[pasutijums]
        return vertiba
    except KeyError:
        return 0

def main():
    summa = 0
    while True:
        try:
            pasutijums = input("Item: ").title()
            summa += noteikt_vertibu(pasutijums)
            print(f"${summa:.2f}")
        except EOFError:
            break
main()