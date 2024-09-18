import random


def main():
    limenis = get_level()
    pareizi = 0
    for i in range(10):
        skaitlis1 = generate_integer(limenis)
        skaitlis2 = generate_integer(limenis)
        cik = 0
        while True:
            try:
                atbilde = int(input(f"{skaitlis1} + {skaitlis2} = "))
                cik += 1
                if atbilde == skaitlis1 + skaitlis2:
                    pareizi += 1
                    break
                elif cik == 3:
                    print(f"{skaitlis1} + {skaitlis2} = {skaitlis1 + skaitlis2}")
                    break
                else:
                    print("EEE")
                    continue
            except ValueError:
                continue
    print(f"Score: {pareizi}")


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n not in [1, 2, 3]:
                continue
            else:
                break
        except:
            continue

    return n

def generate_integer(level):
    if level not in [1, 2, 3]:
        raise ValueError
    elif level == 1:
        return random.randrange(0,10)
    elif level == 2:
        return random.randrange(10,100)
    elif level == 3:
        return random.randrange(100,1000)


if __name__ == "__main__":
    main()