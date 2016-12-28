#!/bin/python3

# https://www.hackerrank.com/challenges/journey-to-the-moon

import unittest


class JourneyToTheMoon:
    def __init__(self, n, known_pairs):
        self.n = n
        self.known_pairs = known_pairs

    def calculate(self):
        # create groups from known pairs
        groups = []

        for (u,v) in self.known_pairs:
            u_group = None
            v_group = None
            for g in groups:
                if u in g:
                    u_group = g
                if v in g:
                    v_group = g
            # merge step
            if u_group and v_group:
                groups.remove(u_group)
                groups.remove(v_group)
                groups.append(u_group.union(v_group))
            elif not u_group and not v_group:
                groups.append(set([u,v]))
            elif u_group:
                groups.remove(u_group)
                groups.append(u_group.union(set([v])))
            elif v_group:
                groups.remove(v_group)
                groups.append(v_group.union(set([u])))

        # compute number of ways in which you can make the combinations
        total_combinations = 0
        group_counts = [len(g) for g in groups]
        for i in range(len(group_counts)):
            for j in range(i+1,len(group_counts)):
                total_combinations += group_counts[i] * group_counts[j]
        return total_combinations


class TestJourneyToTheMoon(unittest.TestCase):
    def test1(self):
        jttm = JourneyToTheMoon(4,[(0,1),(2,3)])
        self.assertEquals(jttm.calculate(),4)


if __name__ == "__main__":
    n, q = [int(x) for x in input().strip().split()]
    known_pairs = []
    for i in range(q):
        known_pairs.append([int(x) for x in input().strip().split()])

    jttm = JourneyToTheMoon(n,known_pairs)
    print(jttm.calculate())