# https://www.hackerrank.com/contests/w27/challenges/hackonacci-matrix-rotations

import unittest

import math


class HackonacciMatrixRotations:
    RECURRING_PATTERN = [0, 1, 0, 0, 1, 1, 1]
    MATRIX_PATTERNS = {1: [1, 0, 0, 0, 0, 1, 1], 2: [0, 0, 1, 1, 0, 0, 1], 3: [0, 1, 0, 0, 1, 0, 1]}
    ROW_KEYS = {90:{1: "1_6", 2: "2_5", 3: "3_4", 4: "3_4", 5: "2_5", 6: "1_6" , 0 : "0"},
                180 : {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6" , 0 : "0"}
                }
    stored_values = { 90: { "0": 0 },
                      180 : {}
                      }

    def __init__(self, n):
        self.n = n
        # self.print_matrix()

    def get_array_element(self, n):
        return self.RECURRING_PATTERN[int((n + 7 - 2) % 7)]

    # def print_matrix(self):
    #     for i in range(1,self.n+1):
    #         print ""
    #         for j in range(1,self.n+1):
    #             print self.get_array_element(i*j*i*j),

    def calculate(self, rotate_angle):
        norm_rotate_angle = rotate_angle % 360
        if norm_rotate_angle == 0:
            return 0

        if self.n % 7 == 6:
            return 0

        if norm_rotate_angle == 270:
            norm_rotate_angle = 90
        count = 0

        for i in range(1, self.n + 1):
            count += self.calculate_for_row(i, norm_rotate_angle)


        return count

    def calculate_for_row(self,row_id,rotate_angle):
        norm_row_id = row_id % 7
        key = self.ROW_KEYS[rotate_angle][norm_row_id]

        if key not in self.stored_values[rotate_angle].keys():
            # calculate how many full lengths are available
            number_of_times_repeated = math.floor(self.n/7)
            # calculate for full length if one full length is available
            full_length_differences = 0
            for i in range(1,8):
                if self.is_different(i, norm_row_id, rotate_angle):
                    full_length_differences += 1
            # calculate for remaining
            remaining_differences = 0
            remaining_count = self.n%7
            for i in range(1,remaining_count+1):
                if self.is_different(i,norm_row_id,rotate_angle):
                    remaining_differences += 1

            self.stored_values[rotate_angle][key] = int(number_of_times_repeated * full_length_differences + remaining_differences)
        return self.stored_values[rotate_angle][key]

    def is_different(self, x, y, rotate_angle):
        if rotate_angle == 90 or rotate_angle == 270:
            rotated_x = y
            rotated_y = self.n - x + 1
        if rotate_angle == 180:
            rotated_x = self.n - x + 1
            rotated_y = self.n - y + 1
        if self.get_array_element(x * y * x * y) != self.get_array_element(rotated_x * rotated_y * rotated_x * rotated_y):
            return True
        return False


class TestHackonacciMatrixRotations(unittest.TestCase):
    def test1(self):
        hmr = HackonacciMatrixRotations(4)
        self.assertEquals(hmr.calculate(90), 10)
        self.assertEquals(hmr.calculate(180), 6)
        self.assertEquals(hmr.calculate(270), 10)

    def test4(self):
        hmr = HackonacciMatrixRotations(10)
        self.assertEquals(hmr.calculate(90), 48)
        self.assertEquals(hmr.calculate(180), 48)
        self.assertEquals(hmr.calculate(270), 48)

    def test5(self):
        hmr = HackonacciMatrixRotations(11)
        self.assertEquals(hmr.calculate(90), 64)
        self.assertEquals(hmr.calculate(180), 54)
        self.assertEquals(hmr.calculate(270), 64)

    def test6(self):
        hmr = HackonacciMatrixRotations(15)
        self.assertEquals(hmr.calculate(90), 104)
        self.assertEquals(hmr.calculate(180), 112)
        self.assertEquals(hmr.calculate(270), 104)

    # def test7(self):
    #     dif = 0
    #     prev = 0
    #     for i in range(6, 15):
    #         hmr = HackonacciMatrixRotations(i)
    #         v = hmr.calculate(90)
    #         dif = v - prev
    #         prev = v
    #         print(i, v)

    def test2(self):
        hmr = HackonacciMatrixRotations(2000)
        self.assertEquals(hmr.calculate(90), 1960244)
        self.assertEquals(hmr.calculate(180), 2449304)
        self.assertEquals(hmr.calculate(270), 1960244)


    def test3(self):
        hmr = HackonacciMatrixRotations(1234)
        self.assertEquals(hmr.calculate(90), 746242)
        self.assertEquals(hmr.calculate(180), 682882)
        self.assertEquals(hmr.calculate(270), 746242)


if __name__ == "__main__":
    n, q = map(int, input().strip().split())
    hmr = HackonacciMatrixRotations(n)
    for i in range(q):
        angle = int(input().strip())
        print(hmr.calculate(angle))
