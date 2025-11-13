lista_1 = [1,2,5,7,2,753,146,87,4,13,7,8,9,100,265,56,77]
prazna_lista = []

def parni_brojevi(lista):
    for broj in lista:
        if broj%2 == 0:
            prazna_lista.append(broj)
    return prazna_lista  
    
print(parni_brojevi(lista_1))
    