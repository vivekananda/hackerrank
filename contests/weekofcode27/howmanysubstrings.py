#!/bin/python3

# https://www.hackerrank.com/contests/w27/challenges/how-many-substrings
# https://www.quora.com/Given-a-string-how-do-I-find-the-number-of-distinct-substrings-of-the-string

import unittest


class HowManySubStrings:
    calculated_values = {}

    def __init__(self, n, q, s):
        self.n = n
        self.q = q
        self.s = s
        pass

    def _get_key(self, left, right):
        return "%d_%d" % (left, right)

    def _lcp(self, str1, str2):
        """LCP = Longest Common Prefix of 2 strings."""
        # print("came to lcp", str1, str2)
        if len(str1) > len(str2):
            str1, str2 = str2, str1

        count = 0
        for i in range(len(str1)):  # str1 will be smaller :)
            if str1[i] == str2[i]:
                count += 1
            else:
                break
        # print("lcp value", count)
        return count

    def calculate(self, left, right):
        key = self._get_key(left, right)
        if key in self.calculated_values.keys():
            return self.calculated_values[key]
        
        sufixes = []
        for i in range(left, right + 1):
            sufixes.append(self.s[i:right + 1])
        # print("sufixes", sufixes)
        sorted_unique_sufixes = list(set(sufixes))
        sorted_unique_sufixes.sort()
        # print("sorted_unique_sufixes", sorted_unique_sufixes)
        # initialize
        uniqueue_substrings = len(sorted_unique_sufixes[0])
        for i in range(1, len(sorted_unique_sufixes)):
            uniqueue_substrings += len(sorted_unique_sufixes[i]) - self._lcp(sorted_unique_sufixes[i - 1],
                                                                             sorted_unique_sufixes[i])
        self.calculated_values[key] = uniqueue_substrings
        return uniqueue_substrings


class TestHowManySubStrings(unittest.TestCase):
    def test1(self):
        hms = HowManySubStrings(5, 5, "aabaa")
        self.assertEquals(hms.calculate(1, 1), 1)
        self.assertEquals(hms.calculate(1, 4), 8)
        self.assertEquals(hms.calculate(1, 1), 1)
        self.assertEquals(hms.calculate(1, 4), 8)
        self.assertEquals(hms.calculate(0, 2), 5)
        pass


if __name__ == "__main__":
    n, q = [int(x) for x in input().strip().split()]
    s = input().strip()
    hms = HowManySubStrings(n, q, s)
    for i in range(q):
        left, right = [int(x) for x in input().strip().split()]
        print(hms.calculate(left, right))
