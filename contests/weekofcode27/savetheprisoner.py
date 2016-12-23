#https://www.hackerrank.com/challenges/save-the-prisoner

import unittest


class Savetheprisoner:

    def __init__(self,n,m,s):
        self.number_of_prisoners =  n
        self.number_of_sweets = m
        self.starting_point = s
    def calculate(self):
        prisoner_num = (self.number_of_sweets + self.starting_point - 1)% self.number_of_prisoners
        if not prisoner_num:
            prisoner_num = self.number_of_prisoners
        return prisoner_num


class TestSavetheprisoner(unittest.TestCase):

    def test1(self):
        stp = Savetheprisoner(5,2,1)
        self.assertEquals(stp.calculate(),2)


    def test2(self):
        stp = Savetheprisoner(5, 7, 1)
        self.assertEquals(stp.calculate(), 2)


    def test3(self):
        stp = Savetheprisoner(5, 5, 5)
        self.assertEquals(stp.calculate(), 4)

    def test4(self):
        stp = Savetheprisoner(1, 7, 1)
        self.assertEquals(stp.calculate(), 1)


    def test5(self):
        stp = Savetheprisoner(5, 10, 2)
        self.assertEquals(stp.calculate(), 1)


if __name__ == "__main__":
    number_of_inputs = int(input().strip())
    for i in range(number_of_inputs):
        (n,m,s) = (int(t) for t in input().strip().split(" "))
        stp = Savetheprisoner(n,m,s)
        print(stp.calculate())
