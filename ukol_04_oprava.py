def test_number(cell_number):
    if len(cell_number) == 9:
        return True
    elif len(cell_number) == 13 and cell_number[:4] == "+420":
        return True   
    else:
        return False
    
cell_number = input("Zadej telefonní číslo: ")
is_number_correct = test_number(cell_number)

if is_number_correct == True:
    message = input("Zadej zprávu: ")
else: 
    print("Zadal jsi chybné číslo.")

print(len(message))

import math

def pay_message(message):
    price_per_180_characters = 3
    number_of_characters = len(message)
    payment = math.ceil(number_of_characters/180) * price_per_180_characters
    return payment

payment = pay_message(message)

print(f'Platba za zprávu je {payment} Kč.')