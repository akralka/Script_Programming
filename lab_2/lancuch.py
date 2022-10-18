# -*- coding: utf-8 -*-

def var(lancuch1, lancuch2):

    return (lancuch1 + lancuch2) *3

def fun(lancuch):
    if lancuch.isdigit():    #jesli wpiszemy liczbę
        exit()
    print(lancuch[0]) 
    print(lancuch[:2]) 
    print(lancuch[2:])
    print(lancuch[-2])
    print(lancuch[-3:])
    print(lancuch[1::2]) 


if __name__ == '__main__':

    res = var('''Programowanie jest 
świetne, każdy tak 
uważa. ''', 
    '''Jeśli ktoś 
twierdzi inaczej 
to się
myli. ''')

    print(res)

    lancuch = '''Python nie pozwala
na łączenie dwóch różnych
typów obiektów'''
    # lancuch = '''14363634634634634'''
    # lancuch = [1,2,3] ???

    fun(lancuch)
    
    # print('słowo'.encode("utf-8"))
    # napisy w Pythonie są niemodyfikowalne 