def main():

    atbilde = sanemt("Fraction: ")
    if 1<atbilde<99:
        print(f"{atbilde}%")
    elif atbilde <= 1:
        print("E")
    elif atbilde >= 99:
        print("F")


def sanemt(jautajums):
    while True:
        x, y = input("Fraction: ").split("/")
        x = int(x)
        y = int(y)
        if x <= y:
            proc = round((x/y*100))
            return proc
        else:
            pass

main()