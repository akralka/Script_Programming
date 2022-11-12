from abc import ABC, abstractmethod
from enum import Enum
from typing import List


class Action(Enum):
    pass

class Lesson:
    pass

class Term:
    pass

class BasicTimetable(ABC):
    @abstractmethod
    def busy(self, term: Term) -> bool:
        pass

    def get(self, term: Term) -> Lesson:
        pass

    @abstractmethod
    def parse(self, actions: List[str]) -> List[Action]:
        pass

    @abstractmethod
    def perform(self, actions: List[Action]):
        pass
  
    @abstractmethod
    def put(self, lesson: Lesson) -> bool:
        pass
##########################################################
class Timetable(BasicTimetable): #children class of BasicTimetable
    def parse(self, actions):
        pass
    def perform(self, actions):
        pass
    def busy(self, term):
        pass

    def get(self, term: Term) -> Lesson:
        print("Wywołano metodę 'get()' zdefiniowaną w klasie 'BasicTimetable'")

    def put(self, lesson: Lesson) -> bool:
        pass


# Sprawdź, czy można tworzyć instancję klasy abstrakcyjnej — 'BasicTimetable'
# timeTable = BasicTimetable() #nie można

# Sprawdź, czy można tworzyć instancję klasy pochodnej — 'Timetable'
timeTable = Timetable() #można

# Wywołujemy metodę, która NIE JEST zdefiniowana w klasie 'Timetable', a w klasie 'BasicTimetable'
timeTable.get(Term())  #można?