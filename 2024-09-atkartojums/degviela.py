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
        cik = input("Fraction: ").split("/")
        try:
            x = int(cik[0])
            y = int(cik[1])
            if x <= y:
                proc = round((x/y*100))
                return proc
            else:
                pass
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

main()