
def sum(arg1, arg2):
    return arg1 + arg2
def fun():
    print(2+2)
    print(2 + 2.0)
    # print(2 + '2')
    print('2' + '2')
    zmienna1 = 2
    print(type(zmienna1))
    zmienna2 = '2'
    print(type(zmienna2))

    print('__name__ = {}'.format(__name__))

if __name__ == '__main__':

    arg1 = int(input())
    arg2 = int(input())
    res = sum(arg1, arg2)
    print("suma:", res)
    fun()





