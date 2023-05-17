class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = True
   
    def pujc_auto(self):
        if self.dostupne:
            self.dostupne = False
            return f'Potvrzuji zapůjčení vozidla {self.registracni_znacka}.'
        else:
            return f'Vozidlo není k dispozici.'
    
    def get_info(self):
        return f'Auto {self.typ_vozidla} s SPZ {self.registracni_znacka}.'

auto1 = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
auto2 = Auto("1P3 4747", "Škoda Octavia", 41253)

pozadavek_uzivatel = input("Vyber auto (Peugeot/Škoda):")

if pozadavek_uzivatel == "Peugeot":
    print(auto1.get_info())
    print(auto1.pujc_auto())
elif pozadavek_uzivatel == "Škoda":
    print(auto2.get_info())
    print(auto2.pujc_auto())   
else:
    print("Zadán chybný název typu auta.")
    
pozadavek_uzivatel = input("Vyber auto (Peugeot/Škoda):")

if pozadavek_uzivatel == "Peugeot":
    print(auto1.get_info())
    print(auto1.pujc_auto())
elif pozadavek_uzivatel == "Škoda":
    print(auto2.get_info())
    print(auto2.pujc_auto())   
else:
    print("Zadán chybný název typu auta.")