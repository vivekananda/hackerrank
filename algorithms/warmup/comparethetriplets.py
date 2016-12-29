#!/bin/python3

import unittest
# https://www.hackerrank.com/challenges/compare-the-triplets

class CompareTheTriplets:
    def __init__(self, a_scores, b_scores):
        self.a_scores = a_scores
        self.b_scores = b_scores

    def calculate(self):
        a_count, b_count = (0, 0)
        for i in range(3):
            if self.a_scores[i] == self.b_scores[i]:
                pass
            elif self.a_scores[i] > self.b_scores[i]:
                a_count += 1
            else:
                b_count += 1
        return (a_count, b_count)


class TestCompareTheTriplets(unittest.TestCase):
    def test1(self):
        ctt = CompareTheTriplets([5, 6, 7], [3, 6, 10])
        self.assertEquals(ctt.calculate(), (1, 1))

    def test2(self):
        ctt = CompareTheTriplets([5, 6, 7], [5, 6, 7])
        self.assertEquals(ctt.calculate(), (0, 0))


if __name__ == "__main__":
    a_values = [int(x) for x in input().strip().split()]
    b_values = [int(x) for x in input().strip().split()]
    ctt = CompareTheTriplets(a_values, b_values)
    (a_value, b_value) = ctt.calculate()
    print(a_value, b_value)
