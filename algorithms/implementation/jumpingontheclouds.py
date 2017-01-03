#!/bin/python

import unittest


# https://www.hackerrank.com/challenges/jumping-on-the-clouds


class Jumping_on_the_clouds:
    n = 0
    c = []

    def __init__(self, n_str, c_str):
        self.n = int(n_str.strip())
        self.c = map(int, c_str.strip().split(" "))

    def calculate_steps(self):
        steps = 0
        i = 0
        while i < self.n - 1:
            if i + 2 < self.n and self.c[i + 2] == 0:
                i += 2
            else:
                i += 1
            steps += 1
        return steps


class Test_jumping(unittest.TestCase):
    def test_input1(self):
        jotc = Jumping_on_the_clouds("7", "0 0 1 0 0 1 0")
        self.assertEquals(jotc.calculate_steps(), 4)

    def test_input2(self):
        jotc = Jumping_on_the_clouds("6", "0 0 0 0 1 0")
        self.assertEquals(jotc.calculate_steps(), 3)


if __name__ == "__main__":
    jotc = Jumping_on_the_clouds(raw_input(), raw_input())
    print(jotc.calculate_steps())
