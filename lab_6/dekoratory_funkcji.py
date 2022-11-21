from inspect import signature

def argumenty(*args, **kwargs):    # args = ([4,5],) len(args) = 1

        def res(funkcja):
            array = []
            array += args[0]     #[4, 5] [4, 5, 6]
            fun_len = len(signature(funkcja).parameters) - 1           # 3 bo sum(1,2,3), 2 bo roznica (1,2)
            def operacja(self, *args, **kwargs):
                arguments = []
                arguments += args  #[[4,5]]
                if([len(args) < fun_len]):
                    val = fun_len - len(args)
                if val > 0:
                    # print(arguments)           # dla op.suma(1,2) [1,2]     dla op.suma(1)   [1]
                    # print(val)                 # 1                                            2
                    # print(array[:val])         # [4]                                         [4,5]
                    arguments += array[:val]
                    # print(arguments)           # dla op.suma(1,2) [1,2,4]                    [1,4,5]
                return funkcja(self, *arguments)
            return operacja
        return res 

class Operacje:

    argumentySuma=[4,5]
    argumentyRoznica=[4,5,6]  

    def __setitem__(self, value, operation):
        if(value == "suma"):
            self.argumentySuma = operation
        elif(value == "roznica"):
            self.argumentyRoznica = operation

    @argumenty(argumentySuma)
    def suma(self,a,b,c):
        return( "%d+%d+%d=%d" % (a,b,c,a+b+c))

    @argumenty(argumentyRoznica)
    def roznica(self,x,y):
        return("%d-%d=%d" % (x,y,x-y))



# op=Operacje()
# op.suma(1,2,3) #Wypisze: 1+2+3=6
# op.suma(1,2) #Wypisze: 1+2+4=7 - 4 jest pobierana z tablicy 'argumentySuma'
# op.suma(1) #Wypisze: 1+4+5=10 - 4 i 5 są pobierane z tablicy 'argumentySuma'
# op.suma() #TypeError: suma() takes exactly 3 arguments (2 given)
# op.roznica(2,1) #Wypisze: 2-1=1
# op.roznica(2) #Wypisze: 2-4=-2
# wynik=op.roznica() #Wypisze: 4-5=-1
# print( wynik) #Wypisze: 6

# op['suma']=[1,2]
# op.argumentySuma

# op['roznica']=[1,2,3]
# op.argumentyRoznica