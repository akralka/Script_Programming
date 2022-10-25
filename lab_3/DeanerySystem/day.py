from enum import Enum


class Day(Enum):
    MON = 1
    TUE = 2
    WED = 3
    THU = 4
    FRI = 5
    SAT = 6
    SUN = 7

    def difference(self, day):
        if day.value - self.value < -3:
            return day.value - self.value + 7
        if day.value - self.value > 3:
            return day.value - self.value - 7
        else:
            return  day.value - self.value


def nthDayFrom(n, day):
        tmp = n % 7
        diff = day.value + tmp
        if diff % 7 == 0:
            diff =  7
        else:
            diff =  diff % 7
        for i in Day:
            if diff == i.value:
                return i





# print(nthDayFrom(1, Day.SAT)) 
# print(nthDayFrom(2, Day.SAT))
# print(nthDayFrom(-1, Day.TUE)) 
# print(nthDayFrom(-2, Day.TUE))
# print(nthDayFrom(8, Day.TUE))

# print(Day.MON.difference(Day.TUE))
# print(Day.MON.difference(Day.SUN))
# print(Day.SUN.difference(Day.MON))
# print(Day.SUN.difference(Day.SAT))

