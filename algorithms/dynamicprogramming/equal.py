#!/usr/bin/env python

# https://www.hackerrank.com/challenges/equal

import unittest


class Equal:
    differences = [5, 2, 1]
    diff_counts = {}

    def __init__(self, arr):
        self.arr = arr

    def calculate(self):
        minimum = min(self.arr)
        counts = []
        for i in range(5):
            if minimum >= i:
                counts.append(self._calculate_for_min(minimum-i))
        return min(counts)

    def _calculate_for_min(self, minimum):
        total_count = 0
        for el in self.arr:
            cur_diff = el - minimum
            total_count += self._count_steps(cur_diff)
        return total_count

    def _count_steps(self, diff):
        key = diff
        if key in self.diff_counts.keys():
            return self.diff_counts[key]
        count = 0
        while diff > 0:
            if diff >= 5:
                diff -= 5
            elif diff >= 2:
                diff -= 2
            elif diff > 0:
                diff -= 1
            count += 1
        self.diff_counts[key] = count
        return count


class TestEqual(unittest.TestCase):
    def test1(self):
        e = Equal([1,2,3])
        self.assertEquals(e.calculate(),2)

    def test2(self):
        e = Equal([1,2,3,4])
        self.assertEquals(e.calculate(),4)

    def test3(self):
        e = Equal([2, 2, 3, 7])
        self.assertEquals(e.calculate(), 2)

    def test4(self):
        e = Equal([0,5])
        self.assertEquals(e.calculate(), 1)

    def test5(self):
        e = Equal([1,1,1,1,1,1,1,6])
        self.assertEquals(e.calculate(), 1)

    def test6(self):
        e = Equal([1,1,1,1,1,1,1,20])
        self.assertEquals(e.calculate(), 5)

    def test7(self):
        e = Equal([1,1,1,1,1,1])
        self.assertEquals(e.calculate(), 0)

    def test8(self):
        e = Equal([7,7,7,4,4,3])
        self.assertEquals(e.calculate(), 6)

    def test9(self):
        e = Equal([1,5,5])
        self.assertEquals(e.calculate(),3)



if __name__ == "__main__":
    t = int(input().strip())
    for i in range(t):
        n = int(input().strip())
        arr = [int(x) for x in input().strip().split()][:n]
        e = Equal(arr)
        print(e.calculate())