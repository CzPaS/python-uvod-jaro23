def test_number(cell_number : str) -> bool:
    correction = cell_number.replace(" ", "")
    if len(correction) == 9:
        return True
    elif len(correction) == 13 and cell_number[:4] == "+420":
        return True   
    else:
        return False
 
cell_number = input("Zadej telefonní číslo: ")
is_number_correct = test_number(cell_number)

import math

def pay_message(message : str) -> int:
    price_per_180_characters = 3
    number_of_characters = len(message)
    payment = math.ceil(number_of_characters/180) * price_per_180_characters
    return payment

if is_number_correct == True:
    message = input("Zadej zprávu: ")
    payment = pay_message(message)
    print(f'Platba za zprávu je {payment} Kč.')
else: 
    print("Zadal jsi chybné číslo.")

