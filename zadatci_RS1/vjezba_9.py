lista_1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 6, 8, 12, 9, 9]
prazna_lista = []

def bez_duplikata(lista):
    for broj in lista:
        if broj not in prazna_lista:
            prazna_lista.append(broj)
    return prazna_lista  
    
print(bez_duplikata(lista_1))