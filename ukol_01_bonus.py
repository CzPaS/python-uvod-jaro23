jmeno_a_prijmeni = input("Zadej prosím své jméno a příjmení: ")
print(jmeno_a_prijmeni.upper())
print(jmeno_a_prijmeni.lower())
velka_pismena = jmeno_a_prijmeni.upper()
seznam = velka_pismena.split()
# ['PAVLA', 'SLABI']
jmeno = seznam[0]
jmeno = jmeno.capitalize() 
prijmeni = seznam [1]
prijmeni = prijmeni.capitalize()
print(jmeno + " " + prijmeni)
print(seznam[0] [0] + "." + seznam [1] [0] + ".")

if len(jmeno) > 5:
    print(seznam [0] [0] + ". " + prijmeni)
