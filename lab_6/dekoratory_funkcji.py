from inspect import signature

def argumenty(*args, **kwargs):

        def inner(funkcja):
            # args = ([4,5],) len(args) = 1
            array =[]
            array += args[0] #[4, 5] [4, 5, 6]
            finalArgs = []
            finalArgs += args #[[4,5]]
            parLen = len(signature(funkcja).parameters) - 1 # 3 bo sum(1,2,3), 2 bo roznica (1,2)

            def operacja(self, *args, **kwargs):
                remaining = 0
                if([len(args) < parLen]):
                    remaining = parLen - len(args)
                if remaining > 0:
                    finalArgs += array[:remaining]
                string = funkcja(self, *finalArgs)
                if type(string) == tuple:
                    if(len(string) > 1):
                        return string[1]
                out = 0
                if len(array) > remaining:
                    out = array[remaining]
                else:
                    out = array[-1]
                return (string, out)
            return operacja
        return inner 


class Operacje:
    argumentySuma=[4,5]
    argumentyRoznica=[4,5,6]  

    def __setitem__(self, key, value):
        if(key == "suma"):
            self.argumentySuma = value
        elif(key == "roznica"):
            self.argumentyRoznica = value

    @argumenty(argumentySuma)
    def suma(self,a,b,c):
        return( "%d+%d+%d=%d" % (a,b,c,a+b+c))

    @argumenty(argumentyRoznica)
    def roznica(self,x,y):
        return("%d-%d=%d" % (x,y,x-y))

# def gfg(x, y):
# 	pass

# t = signature(gfg)

# print(t)

# print(t.parameters['x'])

# op=Operacje()
# op.suma(1,2,3) #Wypisze: 1+2+3=6
# op.suma(1,2) #Wypisze: 1+2+4=7 - 4 jest pobierana z tablicy 'argumentySuma'
# op.suma(1) #Wypisze: 1+4+5=10 - 4 i 5 są pobierane z tablicy 'argumentySuma'
# op.suma() #TypeError: suma() takes exactly 3 arguments (2 given)
# op.roznica(2,1) #Wypisze: 2-1=1
# op.roznica(2) #Wypisze: 2-4=-2
# wynik=op.roznica() #Wypisze: 4-5=-1
# print(wynik) #Wypisze: 

# op['suma']=[1,2]
# oznacza, że   argumentySuma=[1,2]

# #Zmiana zawartości listy argumentów dekoratora  dla metody 'roznica'
# op['roznica']=[1,2,3]
# oznacza, że   argumentyRoznica=[1,2,3]