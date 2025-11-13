class Proizvod:
    def __init__(self, naziv, cijena, dostupna_kolicina):
        self.naziv = naziv
        self.cijena = cijena
        self.dostupna_kolicina = dostupna_kolicina
    
    def ispis(self):
        print(f"Naziv: {self.naziv}, cijena: {self.cijena}, dostupna količina {self.dostupna_kolicina}")
        
skladiste = [Proizvod("Kruh", 1.2, 5), Proizvod("Mlijeko", 0.98, 3)]

def dodaj_proizvod(proizvod):
    skladiste.append(proizvod)
    
