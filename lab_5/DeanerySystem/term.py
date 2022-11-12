from day import Day


class Term():
    def __init__(self, day, hour, minute, duration = 90):
        self.__day = day
        self.hour = hour
        self.minute = minute
        self.duration = duration
        self.time = (day.value -1)*24*60 + hour*60 + minute 

    def __str__(self):
        return f"{Term.method(self._Term__day.value)} {self.hour}:{self.minute} [{self.duration}]"

    def earlierThan(self, termin):
        if self.time < termin.time:
            return True
        return False

    def laterThan(self, termin):
        if self.time > termin.time:
            return True
        return False


    def equals(self, termin):
        if self.time == termin.time:
            return True
        return False

    @staticmethod
    def method(day):
        if day == 1:
            return "PONIEDZIALEK"
        elif day == 2:
            return "WTOREK"
        elif day == 3:
            return "SRODA"
        elif day == 4:
            return "CZWARTEK"
        elif day == 5:
            return "PIATEK"
        elif day == 6:
            return "SOBOTA"
        elif day == 7:
            return "NIEDZIELA"

        
     #  >
    def __gt__(self, termin):
        return self.laterThan(termin)

     #  < 
    def __lt__(self, termin):
        return self.earlierThan(termin)

    #  <= 
    def __le__(self, termin):
        if self.equals(termin):
            return True
        else:
            return self.earlierThan(termin)

    # >=
    def __ge__(self, termin):
        if self.equals(termin):
            return True
        else:
            return self.laterThan(termin)
    
      # == 
    def __eq__(self, termin):
        if self.duration == termin.duration:
            return self.equals(termin)
        else:
            return False

    def __sub__(self, termin):
        return f"{Term.method(termin.__day.value)} {termin.hour}:{termin.minute} [{self.time - termin.time+ self.duration}]"
    

if __name__ =='__main__':

    term1 = Term(Day.MON, 8, 30)
    term2 = Term(Day.TUE, 9, 45, 30)
    term3 = Term(Day.TUE, 9, 45, 90)
    print(term1)
    print(term2)
    print(term3)     
    print("term1 < term2:", term1 < term2)   # Ma się wypisać True
    print("term1 <= term2:", term1 <= term2) # Ma się wypisać True
    print("term1 > term2:", term1 > term2)   # Ma się wypisać False
    print("term1 >= term2:", term1 >= term2) # Ma się wypisać False
    print("term2 == term2:", term2 == term2) # Ma się wypisać True
    print("term2 == term3:", term2 == term3) # Ma się wypisać False
    term4 = term3 - term1                    
    print(term4)                                      

