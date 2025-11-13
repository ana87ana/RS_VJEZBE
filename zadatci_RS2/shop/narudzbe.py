class Narudzba:
    def __init__(self, naruceni_proizvodi, ukupna_cijena):
        self.naruceni_proizvodi = naruceni_proizvodi
        self.ukupna_cijena = ukupna_cijena
    
def napravi_narudzbu(lista):
    naruzba = list(map(lambda x : x["naziv"], lista))
    uk_cijena = sum(lista["cijena"])  
    return Narudzba(naruzba, uk_cijena)      