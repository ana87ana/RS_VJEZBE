from datetime import date
from functools import reduce

#1. Klasa Automobil
class Automobil:
    def __init__(self, marka, model, godina_proizvodnje, kilometraža):
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje
        self.kilometraža = kilometraža
    
    def ispis(self):
        return f"Marka auta: {self.marka}, model auta: {self.model}, godina proizvodnje: {self.godina_proizvodnje}, kilometraža: {self.kilometraža}"
    
    def starost(self):
        return date.today().year - self.godina_proizvodnje

auto = Automobil("Audi", "A7", 2012, 199101)
print(auto.ispis())
print(auto.starost())

#2. Klasa Kalkulator
class Kalkulator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def zbroj(self):
        return self.a + self.b
    
    def oduzimanje(self):
        return self.a - self.b
    
    def mnozenje(self):
        return self.a * self.b
    
    def dijeljenje(self):
        if self.b == 0:
            return f"Dijeljenje s nulom nije moguće!"
        else:
            return self.a / self.b
    
    def potenciranje(self):
        return self.a ** self.b
    
    def korijen(self):
        return self.a ** (1/self.b)

#3. Klasa Student

class Student:
    def __init__(self, ime, prezime, godine, ocjene):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
        self.ocjene = ocjene
        
    def prosjek(self):
        return sum(self.ocjene)/len(self.ocjene)
        
studenti = [
{"ime": "Ivan", "prezime": "Ivić", "godine": 19, "ocjene": [5, 4, 3, 5, 2]},
{"ime": "Marko", "prezime": "Marković", "godine": 22, "ocjene": [3, 4, 5, 2, 3]},
{"ime": "Ana", "prezime": "Anić", "godine": 21, "ocjene": [5, 5, 5, 5, 5]},
{"ime": "Petra", "prezime": "Petrić", "godine": 13, "ocjene": [2, 3, 2, 4, 3]},
{"ime": "Iva", "prezime": "Ivić", "godine": 17, "ocjene": [4, 4, 4, 3, 5]},
{"ime": "Mate", "prezime": "Matić", "godine": 18, "ocjene": [5, 5, 5, 5, 5]}
]

studenti_objetki = list(map(lambda student: Student(student["ime"], student["prezime"], student["godine"], student["ocjene"]), studenti))
najbolji_student = reduce(lambda x, y: x if x.prosjek() > y.prosjek() else y, studenti_objetki)

#4. Klasa Krug

class Krug:
    def __init__(self, r):
        self.r = r
        
    def opseg(self):
        return self.r*2*3.14
    
    def povrsina(self):
        return self.r**2 * 3.14
    
krug = Krug(5)
print(krug.opseg())
print(krug.povrsina())
    
#5 Klasa Radnik

class Radnik:
    def __init__(self, ime, pozicija, placa):
        self.ime = ime
        self.pozicija = pozicija
        self.placa = placa
        
    def work(self):
        return f"Radim na poziciji {self.pozicija}"
    
class Manager(Radnik):
    def __init__(self, ime, pozicija, placa, department):
        super().__init__(ime, pozicija, placa)
        self.department = department
        
    def work(self):
        return f"Radim na poziciji {self.pozicija} u odjelu {self.department}"
    
    def give_raise(self, radnik, povecanje):
        radnik.placa += povecanje
        
radnik_1 = Radnik("marko", "trgovac", 1000)
manager = Manager("iva", "voditeljica", 1200, "prodaja")

manager.give_raise(radnik_1, 50)
print(radnik_1.placa)
        