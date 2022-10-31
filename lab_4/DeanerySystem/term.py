from day import Day


class Term():
    def __init__(self, day, hour, minute, duration):
      self.hour = hour
      self.minute = minute
      self.duration = duration
      self.__day = day

    def __str__(self):
        if self.duration == 0:
            return f"{Term.method(self._Term__day.value)} {self.hour}:{self.minute} [90]"
        else:
            return f"{Term.method(self._Term__day.value)} {self.hour}:{self.minute} [{self.duration}]"

    def earlierThan(self, termin):
        if self.__day.value < termin.__day.value:
            return True
        elif self.__day.value == termin.__day.value:
            if termin.hour > self.hour:
                return True
            if termin.hour == self.hour:
                if termin.minute > self.minute:
                    return True
        return False

    def laterThan(self, termin):
        if self.__day.value > termin.__day.value:
            return True
        elif self.__day.value == termin.__day.value:
            if termin.hour < self.hour:
                return True
            if termin.hour == self.hour:
                if termin.minute < self.minute:
                    return True
        return False


    def equals(self, termin):
        if self.hour == termin.hour and self.minute == termin.minute:
            return True
        return False

    # def tmp(self,termin):
    #     if (Term(self.__day, self.hour, self.minute, self.duration).laterThan(Term(termin.__day, termin.hour, termin.minute, self.duration))):
    #         return False
    #     if (Term(self.__day, self.hour, self.minute, self.duration).laterThan(Term(termin.__day, termin.hour, termin.minute, self.duration))):
    #         if self.duration != termin.duration:
    #             return True
    #         else:
    #             return False
    #     else:
    #         return True

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

    

if __name__ =='__main__':

    term1 = Term(Day.MON, 8, 30, 0)
    term2 = Term(Day.TUE, 9, 45, 30)
    term3 = Term(Day.TUE, 9, 45, 90)
    print(term1)
    print(term2)
    print(term3)
    # print(term1.earlierThan(term2)) 
    # print(term1.laterThan(term2))
    # print(term1.equals(term2))
    # print(Term.tmp(term1, term2))
    # print(Term.tmp(term2, term1))
    # print(Term.tmp(term2, term3))

    
    