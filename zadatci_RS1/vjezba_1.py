a = float(input("Unesite broj: "))
b = float(input("Unesite drugi broj: "))
c = input("Unesite operator: ")
d = ["+", "-", "/", "*", "%", "**"]


if b == 0 and c == "/":
    print("Dijeljenje s nulom nije dozvoljeno!")
elif c not in d:
    print("Nepodržani operator!")
elif c == "+":
    print(a, c, b, "je:", (a+b))
elif c == "-":
    print(a, c, b, "je:", (a-b))
elif c == "/":
    print(a, c, b, "je:", (a/b))
elif c == "**":
    print(a, c, b, "je:", (a**b))
elif c == "*":
    print(a, c, b, "je:", (a*b))
elif c == "%":
    print(a, c, b, "je:", (a%b))