def sendMessage():
    if len(cell_number) == 9:
        message = input("Zadej zprávu: ")
    elif len(cell_number) == 13:
        message = input("Zadej zprávu: ")
    else:
        oprava = cell_number.replace(" ", "")
        print(f'Zadal jsi číslo s mezerou. Zpráva bude zaslána na opravené číslo: {oprava}')
        message = input("Zadej zprávu: ")

    return message, oprava
    
    
cell_number = input("Zadej telefonní číslo: ")
message = sendMessage()
print(len(message))

def payMessage():
    price_per_180_characters = 3
    number_of_characters = len(message)
    if (number_of_characters % 180) != 0:
        payment = ((number_of_characters//180) + 1) * price_per_180_characters
    else:
        payment = number_of_characters * price_per_180_characters
    return payment

payment = payMessage()
print(f'Platba za zprávu je {payment} Kč.')
