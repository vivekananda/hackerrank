#https://www.hackerrank.com/contests/w27/challenges/tailor-shop

import unittest

import math


class TailorShop:

    def __init__(self, x,y):
        self.n,self.p = [int(t) for t in x.strip().split()]
        self.A = map(int, y.strip().split())

    def calculate(self):
        min_number_of_buttons = [ math.ceil(t*1.0/self.p) for t in self.A]
        min_number_of_buttons.sort()
        final_number_of_buttons = []

        max_count_till_now = 0
        sum_of_final_button_counts = 0
        for cur_button_count in min_number_of_buttons:
            if cur_button_count > max_count_till_now:
                sum_of_final_button_counts +=   cur_button_count
                max_count_till_now = cur_button_count
            else:
                max_count_till_now +=1
                sum_of_final_button_counts += max_count_till_now


        return sum_of_final_button_counts


class TestTailorShop(unittest.TestCase):
    def test1(self):
        ts = TailorShop("3 2","4 6 6")
        self.assertEquals(ts.calculate(), 9)

    def test2(self):
        ts = TailorShop("2 3","4 5")
        self.assertEquals(ts.calculate(), 5)

if __name__ == "__main__":
    ts = TailorShop(input(), input())
    print(ts.calculate())

