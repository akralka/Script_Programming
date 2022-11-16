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
            
    def change_time_earlier(self):
        if self.term.minute < (self.term.duration % 60):
            self.term.minute = self.term.minute + 60 - (self.term.duration % 60)
            self.term.hour = self.term.hour - (self.term.duration // 60) - 1
        else:
            self.term.hour = self.term.hour - (self.term.duration // 60)
            self.term.minute = self.term.minute - (self.term.duration % 60)

    def change_time_later(self):
        if self.term.minute + (self.term.duration % 60) >= 60:
            self.term.minute = self.term.minute - 60 + (self.term.duration % 60)
            self.term.hour = self.term.hour + (self.term.duration // 60) + 1
        else:
            self.term.hour = self.term.hour + (self.term.duration // 60)
            self.term.minute = self.term.minute + (self.term.duration % 60)

    def earlierDay(self) -> bool:
        if self.fullTime:
            if self.term._Term__day.value - 1 in [6, 7]:
                return False
            elif self.term._Term__day.value - 1 == 5:
                ending = self.term.hour * 60 + self.term.minute + self.term.duration
                if ending // 60 < 17 and ending // 60 >= 8 or ending == 17 * 60:
                    self.term._Term__day = self.term._Term__day.change(1)
                    return True
            self.term._Term__day = self.term._Term__day.change(1)
            return True

        elif not self.fullTime:
            if self.term._Term__day.value - 1 in [1, 2, 3, 4]:
                return False
            elif self.term._Term__day.value - 1 == 5:
                ending = self.term.hour * 60 + self.term.minute + self.term.duration
                if ending // 60 >= 17 and ending // 60 < 20 or ending == 20 * 60:
                    self.term._Term__day = self.term._Term__day.change(-1)
                    return True
            self.term._Term__day = self.term._Term__day.change(-1)
            return True
        return False

    def laterDay(self) -> bool:
        if self.fullTime:
            if self.term._Term__day.value + 1 in [6, 7]:
                return False
            elif self.term._Term__day.value + 1 == 5:
                ending = self.term.hour * 60 + self.term.minute + self.term.duration
                if ending // 60 < 17 and ending // 60 >= 8 or ending == 17 * 60:
                    self.term._Term__day= self.term.day.change(1)
                    return True
            self.term._Term__day= self.term._Term__day.change(1)
            return True

        elif not self.fullTime:
            if self.term._Term__day.value + 1 in [1, 2, 3, 4]:
                return False
            elif self.term._Term__day.value + 1 == 5:
                ending = self.term.hour * 60 + self.term.minute + self.term.duration
                if ending // 60 >= 17 and ending // 60 < 20 or ending == 20 * 60:
                    self.term._Term__day= self.term.day.change(1)
                    return True
            self.term._Term__day= self.term._Term__day.change(1)
            return True
        return False

    def earlierTime(self):
        if self.fullTime:
            if self.term._Term__day.value in [1,2,3,4]:
                if self.term.hour * 60 + self.term.minute - self.term.duration >= 480 and self.term.hour * 60 + self.term.minute + self.term.duration <= 1200:
                    self.change_time_earlier()
                    return True
            if self.term._Term__day.value == 5:
                if self.term.hour * 60 + self.term.minute - self.term.duration >=480 and self.term.hour * 60 + self.term.minute + self.term.duration <1020:
                    self.change_time_earlier()
                    return True
            return False
                
        elif not self.fullTime:
            if self.term._Term__day.value in [6,7]:
                if self.term.hour * 60 + self.term.minute - self.term.duration >=480 and self.term.hour * 60 + self.term.minute + self.term.duration <=1200:
                    self.change_time_earlier()
                    return True
            if self.term._Term__day.value == 5:
                if self.term.hour * 60 + self.term.minute - self.term.duration >=1020 and self.term.hour * 60 + self.term.minute + self.term.duration <= 1200:
                    self.change_time_earlier()
                    return True
            return False


    def laterTime(self):
        if self.fullTime:
            if self.term._Term__day.value in [1,2,3,4]:
                if self.term.hour * 60 + self.term.minute - self.term.duration >= 480 and self.term.hour * 60 + self.term.minute + self.term.duration <= 1200:
                    self.change_time_later()
                    return True
            if self.term._Term__day.value == 5:
                if self.term.hour * 60 + self.term.minute - self.term.duration >=480 and self.term.hour * 60 + self.term.minute + self.term.duration <1020:
                    self.change_time_later()
                    return True
            return False
                
        elif not self.fullTime:
            if self.term._Term__day.value in [6,7]:
                if self.term.hour * 60 + self.term.minute - self.term.duration >=480 and self.term.hour * 60 + self.term.minute + self.term.duration <=1200:
                    self.change_time_later()
                    return True
            if self.term._Term__day.value == 5:
                if self.term.hour * 60 + self.term.minute - self.term.duration >=1020 and self.term.hour * 60 + self.term.minute + self.term.duration <= 1200:
                    self.change_time_later()
                    return True
            return False

# python -i .\lesson.py
#  lesson = Lesson(Term(Day.TUE, 9, 40), "Programowanie skryptowe", "Stanisław Polak", 2)
# print(lesson)