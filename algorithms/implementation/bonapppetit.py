#!/bin/python

import unittest


# https://www.hackerrank.com/challenges/bon-appetit


class BonAppitit:
    n = 0
    k = 0
    costs = []
    b_charged = 0

    def __init__(self, n_str, costs_str, b_str):
        self.n, self.k = map(int, n_str.strip().split(" "))
        self.costs = map(int, costs_str.strip().split(" "))
        self.b_charged = int(b_str.strip())

    def check_bill(self):
        b_actual = (sum(self.costs) - self.costs[self.k]) / 2
        diff = self.b_charged - b_actual
        if diff:
            print diff
        else:
            print "Bon Appetit"

        return diff


class TestBonAppitit(unittest.TestCase):
    def test_input1(self):
        ba = BonAppitit("4 1", "3 10 2 9", "12")
        self.assertEquals(ba.check_bill(), 5)


    def test_input3(self):
        ba = BonAppitit("4 1", "3 10 2 9", "7")
        self.assertEquals(ba.check_bill(), 0)


if __name__ == "__main__":
    ba = BonAppitit(raw_input(), raw_input(), raw_input())
    ba.check_bill()
