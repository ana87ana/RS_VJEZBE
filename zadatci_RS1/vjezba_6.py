
suma = 0
for broj in range(1, 101):
    if broj%2 == 0:
        suma += broj
        
print(suma)


for broj in range(20, 0, -1):
    if broj%2 != 0:
        print(broj)

a = 0
b = 1

print(a)
print(b)
for broj in range(15):
    zbroj = a + b
    print(zbroj)
    a = b
    b = zbroj