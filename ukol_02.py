sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

soucastka = input("Jaký je kód součástky: ")

if soucastka in sklad:
    print(f'Požadovaná součástka {soucastka} je skladem.')
    pozadovane_mnozstvi = int(input("Kolik kusů je požadováno: "))
    if pozadovane_mnozstvi >= sklad[soucastka]:
        print(f'Lze prodat maximálně {sklad[soucastka]} kusů.')
        odeber = sklad.pop(soucastka)
        print(f'Položka {soucastka} byla vyprodána a odebrána ze skladu.')
        print(f'Aktuální stav celého skladu je: {sklad}')
    else:
        print(f'Součástka je na skladě v požadovaném množství {pozadovane_mnozstvi} kusů.')
        sklad[soucastka] -= pozadovane_mnozstvi
        print(f'Aktualizovaný stav zásob součástky {soucastka} je {sklad[soucastka]} kusů.')
        print(f'Aktuální stav celého skladu je: {sklad}')

else:
    print("Požadovaná součástka není skladem.")
    exit()



