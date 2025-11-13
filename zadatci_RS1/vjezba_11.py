
lista_1 = []
lista_2 = []

def grupiraj(lista):
    for broj in lista:
        if broj%2 == 0:
            lista_1.append(broj)
        else:
            lista_2.append(broj)
            
    
    return 