from day import Day


class Term():
    def __init__(self, day: Day, hour: int, minute: int, time: int = 90):
        self.__day = None
        self.__hour = None
        self.__minute = None
        self.__duration = None
        self.__time = None
        self.__beginning = None
        self.__ending = None

    def __str__(self):
        return f"{Term.method(self.day.value)} {self.hour}:{self.minute} [{self.duration}]"
    @property
    def day(self):
        return self.__day
    
    @day.setter
    def day(self, day):
        self.__day = day

    @property
    def hour(self):
        return self.__hour
    
    @hour.setter
    def hour(self, hour):
        self.__hour = hour

    @property
    def minute(self):
        return self.__minute
    
    @minute.setter
    def minute(self, minute):
        self.__minute = minute

    @property
    def duration(self):
        return self.__duration
    
    @duration.setter
    def duration(self, duration):
        self.__duration = duration

    @property
    def _time(self):
        return self.__time
    
    @_time.setter
    def _time(self, day, hour, minute):
        self.__time = (day.value - 1) * 24 * 60 + hour * 60 + minute

    @property
    def _beginning(self):
        return self.__beginning
    
    @_beginning.setter
    def _beginning(self, _time):
        self.__beginning = _time % (24 * 60)

    @property
    def _ending(self):
        return self.__ending

    @_ending.setter
    def _ending(self, _time):
        self.__ending = self.term._time % (24 * 60) + self.term.duration
    
    @property
    def _beginning(self):
        return self.__beginning
    
    @_beginning.setter
    def _beginning(self, _time):
        self.__beginning = _time % (24 * 60)

    @property
    def _ending(self):
        return self.__ending

    @_ending.setter
    def _ending(self, _time):
        self.__ending = self.term._time % (24 * 60) + self.term.duration

    def validate(self):
        if self.fullTime:
            if self.term.day.value in [6, 7]:
                print("Wrong term! Change it")
            elif self.term.day.value == 5:
                if self._beginning < 8 * 60 or self._ending > 17 * 60:
                    print("Wrong term! Change it")

        elif not self.fullTime:
            if self.term.day.value in [1, 2, 3, 4]:
                print("Wrong term! Change it")
            elif self.term.day.value == 5:
                if self._beginning < 17 * 60 or self._ending > 20 * 60:
                    print("Wrong term! Change it")

    def change(self, duration, time=True, beginning=True, ending=True):
        if time:
            self._time += duration
        if beginning:
            self._beginning += duration
        if ending:
            self._ending += duration


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
    

# if __name__ =='__main__':

#     term1 = Term(Day.MON, 8, 30)
#     term2 = Term(Day.TUE, 9, 45, 30)
#     term3 = Term(Day.TUE, 9, 45, 90)
#     print(term1)
#     print(term2)
#     print(term3)     
#     print("term1 < term2:", term1 < term2)   # Ma się wypisać True
#     print("term1 <= term2:", term1 <= term2) # Ma się wypisać True
#     print("term1 > term2:", term1 > term2)   # Ma się wypisać False
#     print("term1 >= term2:", term1 >= term2) # Ma się wypisać False
#     print("term2 == term2:", term2 == term2) # Ma się wypisać True
#     print("term2 == term3:", term2 == term3) # Ma się wypisać False
#     term4 = term3 - term1                    
#     print(term4)                                      
