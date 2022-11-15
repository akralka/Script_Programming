from term import Term
from day import Day
from TimetableWithoutBreaks import TimetableWithoutBreaks

class Lesson():
    def __init__(self, timetable: TimetableWithoutBreaks, term: Term, name: str, teacherName: str, year: str, fullTime: bool = True):
        self.name = None
        self.teacherName = None
        self.year = None
        self.term = None
        self.fullTime = None
        self.__timetable = None
    
    def __str__(self):
            if self.fullTime:
                self.fullTime = "stacjonarnych"
            if not self.fullTime:
                self.fullTime = "niestacjonarne"
            return f"{self.name} ({Term.method(self.term._Term__day.value)} {self.term.hour}:{self.term.minute}-{(self.term.hour + (self.term.duration // 60) + ((self.term.minute +(self.term.duration % 60)) // 60))}:{(self.term.minute +   self.term.duration) % 60})\
            \n{self.year} rok studiów {self.fullTime}\
            \nProwadzący: {self.teacherName}"

    @property
    def timetable(self):
        return self._timetable

    @timetable.setter
    def timetable(self, timetable):
        self.__timetable = timetable

    @property
    def term(self):
        return self.__term
    
    @term.setter
    def term(self, term):
        self.__term = term

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def teacherName(self):
        return self.__teacherName
    
    @teacherName.setter
    def teacherName(self, teacherName):
        self.__teacherName = teacherName

    @property
    def year(self):
        return self.__year
    
    @year.setter
    def year(self, year):
        self.__year = year

    @property
    def fullTime(self):
        return self.__fullTime
    
    @fullTime.setter
    def fullTime(self, fullTime):
        self.__fullTime = fullTime

    def change(self, duration, time=True, beginning=True, ending=True):
        if time:
            self._time += duration
        if beginning:
            self._beginning += duration
        if ending:
            self._ending += duration

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
        if not TimetableWithoutBreaks.can_be_transferred_to(Term(self.term.day.change(-1), self.term.hour, self.term.minute), self.term.fullTime):
            return False
        if TimetableWithoutBreaks.busy(self.term):
            return False
        self.term.day = self.term.day.change(-1)
        self.term.change(-24*60)
        return True

    def laterDay(self) -> bool:
        if TimetableWithoutBreaks.can_be_transferred_to(Term(self.term.day.change(1), self.term.hour, self.term.minute), self.term.fullTime):
            return False
        if TimetableWithoutBreaks.busy(self.term):
            return False
        self.term.day = self.term.day.change(1)
        self.term.change(24*60)
        return True

    def earlierTime(self):
        if TimetableWithoutBreaks.can_be_transferred_to(Term(self.term.day, self.term.hour - self.term.duration // 60, self.term.minute - self.term.duration % 60), self.term.fullTime):
            return False
        if TimetableWithoutBreaks.busy(self.term):
            return False
        self.change_time_earlier()
        return True


    def laterTime(self):
        if TimetableWithoutBreaks.can_be_transferred_to(Term(self.term.day, self.term.hour + self.term.duration // 60, self.term.minute + self.term.duration % 60), self.term.fullTime):
            return False
        if TimetableWithoutBreaks.busy(self.term):
            return False
        self.change_time_later()
        return True
