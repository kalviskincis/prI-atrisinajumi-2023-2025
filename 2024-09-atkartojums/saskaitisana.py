izteiksme = input("Expression :")
x, z, y = izteiksme.split(" ")
x1 = float(x)
y1 = float(y)
if z == "+":
    print(x1+y1)
elif z == "-":
    print(x1-y1)
elif z == "*":
    print(x1*y1)
elif z == "/":
    print(x1/y1)
    