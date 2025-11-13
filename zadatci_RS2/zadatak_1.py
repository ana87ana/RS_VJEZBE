#kvadriranje broja
print((lambda x : x ** 2)(4))

#zbroji pa kvadriraj
print((lambda x, y : (x+y)**2)(3,2))

#kvadriraj duljinu niza
print((lambda niz : len(niz)**2)("pozdrav"))

#pomnoži vrijednost s 5 pa potenciraj na x
print((lambda x, y : (y * 5)**x)(2, 4))

#vrati True ake je broj paran, inače vrati None
print((lambda x : True if x%2 == 0 else None)(3))

