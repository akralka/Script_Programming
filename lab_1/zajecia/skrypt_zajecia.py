magazine = {'T-shirt': 34, 'Dress': 22, 'Skirt': 54, 'Jumper': 66, 
            'Shoes': 45, 'Socks': 76, 'Jeans': 33}


def sale(product, quantity, name):

    if product not in magazine.keys():
        return "Nieprawidłowy produkt\n"

    if name == '':
        return 'Brak nazwiska\n'

    if isinstance(quantity, str):
        if not quantity.isdigit():
            return 'Nieprawidłowa ilość\n'
        else:
            quantity = int(quantity)
        
    if quantity > magazine[product]:
        return 'Za duża ilość\n'

    if quantity <= 0:
        return "Ilość mniejsza lub równa 0\n"
        
    for letter in name.lower():
        if letter not in 'abcdefghijklmnoprstuvwxyzq':
            return "Niepoprawne nazwisko\n"

    magazine[product] -= quantity

    return f'{name} kupil {quantity} {product}\n'



def refund(product, quantity, name):

    if product not in magazine.keys():
        return "Nieprawidłowy produkt\n"

    if name == '':
        return 'Brak nazwiska\n'
    
    if isinstance(quantity, str):
        if not quantity.isdigit():
            return 'Nieprawidłowa ilość\n'
        else:
            quantity = int(quantity)

    if quantity <= 0:
        return "Ilość mniejsza lub równa 0\n"


    for letter in name.lower():
        if letter not in 'abcdefghijklmnoprstuwvxyzq':
            return "Niepoprawne nazwisko\n"

    magazine[product] += quantity

    return f'{name} zwrocil {quantity} {product}\n'
            

if __name__=='__main__':
    try:
        with open("logs.txt", 'w') as file: 
            file.write('')        
        with open("logs.txt", 'a') as file: 
            while True:
                transaction = input().split()

                if transaction[0] == 'sale':
                    file.write(sale(transaction[1], transaction[2], transaction[3]))

                elif transaction[0] == 'refund':
                    file.write(refund(transaction[1], transaction[2], transaction[3]))

    except(EOFError):
        with open("logs.txt", "r") as file:
            print(file.read()) 
            print(magazine)




