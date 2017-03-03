#!/bin/python3

import unittest


class DayOfTheProgrammer():
    def compute(self, y):

        diff = 13
        if y == 1918:
            diff += 13
        elif y < 1918:
            if y % 4 == 0:
                diff -= 1
        else:
            if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
                diff -= 1

        programmer_day_str = ""
        if diff > 0:
            programmer_day_str = "%2d.09.%d" % (diff, y)
        else:
            programmer_day_str = "31.08.%d" % (y,)
        print(programmer_day_str)
        return programmer_day_str

    pass


class TestDayOfTheProgrammer(unittest.TestCase):
    def test1(self):
        dotp = DayOfTheProgrammer()
        self.assertEquals(dotp.compute(2017), "13.09.2017")
        self.assertEquals(dotp.compute(2016), "12.09.2016")
        self.assertEquals(dotp.compute(1918), "26.09.1918")
        self.assertEquals(dotp.compute(1916), "12.09.1916")


if __name__ == "__main__":
    y = int(input().strip())

    dotp = DayOfTheProgrammer()
    dotp.compute(y)
