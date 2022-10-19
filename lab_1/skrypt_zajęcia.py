magazine = {'T-shirt': 34, 'Dress': 22, 'Skirt': 54, 'Jumper': 66, 
            'Shoes': 45, 'Socks': 76, 'Jeans': 33}

logs = []

def sale(product, quantity, name):

    if product not in magazine.keys():
        return "Nieprawidłowy produkt"

    if name == '':
        return 'Brak nazwiska'

    if isinstance(quantity, str):
        if not quantity.isdigit():
            return 'Nieprawidłowa ilość'
        else:
            quantity = int(quantity)
        
    if quantity > magazine[product]:
        return 'Za duża ilość'

    if quantity <= 0:
        return "Ilość mniejsza lub równa 0"

    
        
    for letter in name.lower():
        if letter not in 'abcdefghijklmnoprstuvxyzq':
            return "Niepoprawne nazwisko"

    logs.append(f'{name} kupił {quantity} {product}')



def refund(product, quantity, name):

    if product not in magazine.keys():
        return "Nieprawidłowy produkt"

    if name == '':
        return 'Brak nazwiska'
    
    if isinstance(quantity, str):
        if not quantity.isdigit():
            return 'Nieprawidłowa ilość'
        else:
            quantity = int(quantity)

    if quantity <= 0:
        return "Ilość mniejsza lub równa 0"


    for letter in name.lower():
        if letter not in 'abcdefghijklmnoprstuvxyzq':
            return "Niepoprawne nazwisko"

    

    logs.append(f'{name} zwrócił {quantity} {product}')
            

if __name__=='__main__':
    try:

        while True:
            transaction = input().split()

            if transaction[0] == 'sale':
                sale(transaction[1], transaction[2], transaction[3])

            elif transaction[0] == 'refund':
                refund(transaction[1], transaction[2], transaction[3])

    except(EOFError):
        print(logs)





