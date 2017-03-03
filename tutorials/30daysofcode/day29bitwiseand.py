#!/usr/bin/env python

import unittest

# https://www.hackerrank.com/challenges/30-bitwise-and?h_r=next-challenge&h_v=zen


import sys


class Bitwiseand:
    def compute(self, n, k):
        """
        calculated_value = 0
        least_significant_bit = 1
        temp_n = n
        while (temp_n):
            if temp_n % 2 == 1:
                break
            least_significant_bit *= 2
            temp_n /= 2
        max_possible = ((n - least_significant_bit) | int(int((least_significant_bit - 1) / 2) * 2))
        if k - 1 <= max_possible:
            calculated_value = k - 1
        else:
            calculated_value = max_possible
        """

        calculated_value = k - 1 if ((k - 1) | k) <= n else k - 2
        print(calculated_value)
        return calculated_value


class TestBitwiseand(unittest.TestCase):
    def test1(self):
        bwa = Bitwiseand()
        self.assertEquals(bwa.compute(5, 2), 1)

    def test2(self):
        bwa = Bitwiseand()
        self.assertEquals(bwa.compute(8, 5), 4)

    def test3(self):
        bwa = Bitwiseand()
        self.assertEquals(bwa.compute(2, 2), 0)

    def test4(self):
        bwa = Bitwiseand()
        self.assertEquals(bwa.compute(1025, 500), 499)

    def test5(self):
        bwa = Bitwiseand()
        self.assertEquals(bwa.compute(207, 128), 126)




if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n, k = input().strip().split(' ')
        n, k = [int(n), int(k)]
        bwa = Bitwiseand()
        bwa.compute(n, k)
