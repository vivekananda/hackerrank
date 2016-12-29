#!/bin/python3

import unittest


# https://www.hackerrank.com/challenges/a-very-big-sum



class AVeryBigSum:

    def __init__(self,arr):
        self.arr
    def calculate(self):
        return sum(self.arr)

class TestAVeryBigSum(unittest.TestCase):
    def test1(self):
        avbs = AVeryBigSum([int(x) for x in "1000000001 1000000002 1000000003 1000000004 1000000005".strip().split()])
        self.assertEquals(avbs.calculate(),5000000015)

if __name__ == "__main__":
    avbs = AVeryBigSum([int(x) for x in input().strip().split()])
    print(avbs.calculate())