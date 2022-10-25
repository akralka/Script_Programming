# from day import Day


class Term():
    def __init__(self, day, hour, minute):
      self.hour = hour
      self.minute = minute
      self.duration = 90
      self.__day = day

    def __str__(self):
        return f"{Term.method(self._Term__day.value)} {self.hour}:{self.minute} [{self.duration}]"

    def earlierThan(self, termin):
        if termin.hour > self.hour:
            return True
        if termin.hour == self.hour:
            if termin.minute > self.minute:
                return True
        return False

    def laterThan(self, termin):
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

    

# if __name__ =='__main__':

#     term1 = Term(Day.TUE, 9, 45)
#     term2 = Term(Day.WED, 10, 15)
#     print(term1)
#     print(term2)
#     print(term1.equals(term2))
#     print(term1.laterThan(term2))
#     print(term1.earlierThan(term2)) 