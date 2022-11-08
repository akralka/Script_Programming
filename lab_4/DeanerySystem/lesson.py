from term import Term
from day import Day

class Lesson():
    def __init__(self, term:Term, name:str, teacherName:str, year:int):
        self.name = name
        self.teacherName = teacherName
        self.year = year
        self.term = Term()

    def __str__(self):
        return f"{Term.method(self._Term__day.value)} {self.hour}:{self.minute} [{self.duration}]"

        

if __name__ =='__main__':

    term1 = Term(Day.SAT, 8, 30, 40)
    print(term1)
