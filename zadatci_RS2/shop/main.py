import proizvod as p
import narudzbe as n

proizvodi_za_dodavanje = [
{"naziv": "Laptop", "cijena": 5000, "dostupna_kolicina": 10},
{"naziv": "Monitor", "cijena": 1000, "dostupna_kolicina": 20},
{"naziv": "Tipkovnica", "cijena": 200, "dostupna_kolicina": 50},
{"naziv": "Miš", "cijena": 100, "dostupna_kolicina": 100}
]

p.skladiste = list(map(lambda item: p.Proizvod(item["naziv"], item["cijena"], item["dostupna_kolicina"]), proizvodi_za_dodavanje))

for item in p.skladiste:
    item.ispis()
    
n.napravi_narudzbu(p.skladiste)