#!/usr/bin/env python

import unittest


# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list

class FindSecondLargest:
    def __init__(self, arr):
        self.arr = arr

    def find(self):
        m1 = -100000
        m2 = -100000
        for el in self.arr:
            if el > m1:
                if m1 > m2:
                    m2 = m1
                m1 = el
            else:
                if el > m2 and el != m1:
                    m2 = el
        return m2


class TestFindSecondLargest(unittest.TestCase):
    r1 = [0, 1, 2, 3, 4]
    r2 = [5, 6, 7, 8, 9]
    rr1 = [0, 1, 2, 3, 4]
    rr1.reverse()
    rr2 = [5, 6, 7, 8, 9]
    rr2.reverse()

    def test1(self):
        fsl = FindSecondLargest(self.r1 + self.r2)
        self.assertEquals(fsl.find(), 8)

    def test2(self):
        fsl = FindSecondLargest(self.r1 + self.rr2)
        self.assertEquals(fsl.find(), 8)

    def test3(self):
        fsl = FindSecondLargest(self.rr2 + self.rr1)
        self.assertEquals(fsl.find(), 8)

    def test4(self):
        fsl = FindSecondLargest(self.rr1 + self.rr2)
        self.assertEquals(fsl.find(), 8)

    def test5(self):
        fsl = FindSecondLargest(self.rr1 + self.r2)
        self.assertEquals(fsl.find(), 8)

    def test6(self):
        fsl = FindSecondLargest(self.r1 + self.rr2)
        self.assertEquals(fsl.find(), 8)

    def test7(self):
        fsl = FindSecondLargest(self.r1 + self.r1 + self.rr2)
        self.assertEquals(fsl.find(), 8)

    def test8(self):
        fsl = FindSecondLargest(self.rr1 + self.r1 + self.rr2)
        self.assertEquals(fsl.find(), 8)

    def test9(self):
        fsl = FindSecondLargest(self.r1 + self.rr2 + [8] * 10)
        self.assertEquals(fsl.find(), 8)

    def test10(self):
        fsl = FindSecondLargest(self.r1 + self.rr2 + [9] * 10)
        self.assertEquals(fsl.find(), 8)


if __name__ == "__main__":
    n = input()
    fsl = FindSecondLargest(map(int, input().strip().split()))
    print(fsl.find())
