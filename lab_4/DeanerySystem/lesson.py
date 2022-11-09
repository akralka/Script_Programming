from term import Term
from day import Day

class Lesson():
    def __init__(self, term, name:str, teacherName:str, year:int, fullTime=True):
        self.name = name
        self.teacherName = teacherName
        self.year = year
        self.term = term
        self.fullTime = fullTime

    def __str__(self):
            if self.fullTime:
                self.fullTime = "stacjonarnych"
            if not self.fullTime:
                self.fullTime = "niestacjonarne"
            return f"{self.name} ({Term.method(self.term._Term__day.value)} {self.term.hour}:{self.term.minute}-{(self.term.hour + (self.term.duration // 60) + ((self.term.minute +(self.term.duration % 60)) // 60))}:{(self.term.minute +   self.term.duration) % 60})\
            \n{self.year} rok studiów {self.fullTime}\
            \nProwadzący: {self.teacherName}"

    def earlierDay(self):
        if self.fullTime is True:
            if self.term._Term__day.value in [1,7]:
                return False
            elif self.term._Term__day.value == 6:
                end = self.term.hour * 60 + self.term.minute + self.term.duration
                if end // 60 < 17 and end // 60 >= 8 or end == 17 * 60:
                    self.term._Term__day.value = self.term._Term__day.value -  1
                    return True
            self.term._Term__day.value = self.term._Term__day.value -  1
            return True

        elif not self.fullTime:
            if self.term._Term__day.value == 6:
                ending = self.term.hour * 60 + self.term.minute + self.term.duration
                if ending // 60 >= 17 and ending // 60 < 20 or ending == 20 * 60:
                    self.term.__day = self.term.__day -  1
                    return True
            if self.term._Term__day.value  in [2, 3, 4, 5]:
                return False
            self.term._Term__day.value = self.term._Term__day.value -  1
            return True
        return False

    def laterDay(self):
        if self.fullTime is True:
            if self.term._Term__day.value + 1 in [6, 7]:
                return False
            elif self.term._Term__day.value + 1 == 5:
                end = self.term.hour * 60 + self.term.minute + self.term.duration
                if end // 60 < 17 and end // 60 >= 8 or end == 17 * 60:
                    self.term._Term__day.value += 1
                    return True
            self.term._Term__day.value += 1
            return True

        elif not self.fullTime:
            if self.term._Term__day.value + 1 in [1, 2, 3, 4]:
                return False
            elif self.term._Term__day.value + 1 == 5:
                ending = self.term.hour * 60 + self.term.minute + self.term.duration
                if ending // 60 >= 17 and ending // 60 < 20 or ending == 20 * 60:
                    self.term._Term__day += 1
                    return True
            self.term._Term__day += 1
            return True
        return False


 