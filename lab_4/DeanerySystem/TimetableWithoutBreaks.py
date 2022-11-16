from __future__ import annotations
from typing import List, TYPE_CHECKING
if TYPE_CHECKING :
    from term import Term
    from lesson import Lesson

from enum import Enum
from math import floor
import re



class Action(Enum):
    DAY_EARLIER = 0
    DAY_LATER = 1
    TIME_EARLIER = 2
    TIME_LATER = 3


class TimetableWithoutBreaks:
    def __init__(self):
        self.lessons = []

    def can_be_transferred_to(self, term: Term, fullTime: bool) -> bool:

        if fullTime:
            if term.day.value in [6, 7]:
                return False
            elif term.day.value == 5:
                if self.term. _beginning >= 8 * 60 and self.term._ending <= 17 * 60:
                    return True
            elif term.day.value in [1, 2, 3, 4]:
                if self.term._ending <= 20 * 60 and self.term._beginning >= 8 * 60:
                    return True
        else:
            if term.day.value in [1, 2, 3, 4]:
                return False
            elif term.day.value == 5:
                if self.term._beginning >= 17 * 60 and self.term._ending <= 20 * 60:
                    return True
            elif term.day.value in [6, 7]:
                if self.term._ending <= 20 * 60 and self.term._beginning >= 8 * 60:
                    return True

    def busy(self, term: Term):

        if not term in self.lessons:
            return False
        return True

    def put(self, lesson: Lesson):
        if(self.can_be_transferred_to(lesson.term, lesson.fullTime)):
            self.lessons.append(lesson)
            return True
        return False

    def remove(self, term: Term):
        for i,lesson in enumerate(self.lessons):
            if(lesson.term == term):
                self.lessons.pop(i)
                return True
        return False

    def replace(self, lesson: Lesson):
        self.remove(lesson.term)
        return self.put(lesson)

    def parse(self, actions: List[str]) -> List[Action]:
        reg = re.compile(r'^d\+$|^t\+$|^d-$|^t-$')
        i = 0
        while i < len(actions):
            if reg.match(actions[i]):
                i += 1
            else:
                actions.pop(i)
        translate = {"d+":Action.DAY_LATER, 
            "d-":Action.DAY_EARLIER, 
            "t-":Action.TIME_EARLIER, 
            "t+":Action.TIME_LATER}
        result = []
        for each in actions:
            result.append(translate[each])
        return result                

    @staticmethod
    def align(string):
        if(len(string) > 20):
            return string[:20]
        else:
            i = (20-len(string))/2
            if(i % 1):
                i = floor(i)
                return " "*i + string + " "*(i+1)
            else:
                i = int(i)
                return " "*i + string + " "*i


    def perform(self, actions: List[Action]):
        for i in range(len(actions)):
            if(actions[i] == Action.DAY_EARLIER):
                self.lessons[i%len(self.lessons)].earlierDay()
            elif(actions[i] == Action.DAY_LATER):
                self.lessons[i%len(self.lessons)].laterDay()
            elif(actions[i] == Action.TIME_LATER):
                self.lessons[i%len(self.lessons)].laterTime()
            elif(actions[i] == Action.TIME_EARLIER):
                self.lessons[i%len(self.lessons)].earlierTime()


    def __str__(self):
        out = " "*20
        for i in range(0,7):
            out += "*" + TimetableWithoutBreaks.align(Day(i).readable())
        out += "\n" + "*"*(8*20+7) + "\n"
        start = Term.fromInt(480)
        end = Term.fromInt(570)
        for i in range(0,8):
            time = str(start)[:-5] + "-" + str(end)[:-5]
            out += TimetableWithoutBreaks.align(time)
            for j in range(0,7):
                lesson = self.get(Term.fromInt(int(start)+1440*j))
                if(lesson == None):
                    out += "*" + " "*20 
                else:
                    out += "*" + TimetableWithoutBreaks.align(lesson.name)
            start.rebuildFromMinutes(int(start)+90)
            end.rebuildFromMinutes(int(end)+90)
            out += "\n" + "*"*(8*20+7) + "\n"
        return out