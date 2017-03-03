import unittest

import math

# https://www.hackerrank.com/contests/w28/challenges/lucky-number-eight

MULTIPLESOFEIGHT = {1: [0, 8],
                    2: [00, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96],
                    3: [000, 104, 112, 120, 128, 136, 144, 152, 160,
                        168, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248, 256, 264, 272, 280, 288, 296, 304, 312,
                        320,
                        328, 336, 344, 352, 360, 368, 376, 384, 392, 400, 408, 416, 424, 432, 440, 448, 456, 464, 472,
                        480,
                        488, 496, 504, 512, 520, 528, 536, 544, 552, 560, 568, 576, 584, 592, 600, 608, 616, 624, 632,
                        640,
                        648, 656, 664, 672, 680, 688, 696, 704, 712, 720, 728, 736, 744, 752, 760, 768, 776, 784, 792,
                        800,
                        808, 816, 824, 832, 840, 848, 856, 864, 872, 880, 888, 896, 904, 912, 920, 928, 936, 944, 952,
                        960,
                        968, 976, 984, 992]
                    }


class LuckyNumberEight:
    def __init__(self, number):
        self.input_str = number

    def check_lucky_number_eight(self):

        count = 0
        modulo_var = math.pow(10, 9) + 7

        length_of_number = len(self.input_str)
        # count single digit numbers
        for i in range(length_of_number):
            if int("".join([self.input_str[i], ])) in MULTIPLESOFEIGHT[1]:
                count += 1
        count = count % modulo_var
        # count for double digit number
        for i in range(length_of_number - 1):
            for j in range(i + 1, length_of_number):
                if int("".join([self.input_str[i], self.input_str[j]])) in MULTIPLESOFEIGHT[2]:
                    count += 1
        count = count % modulo_var

        # count for tripple digit number
        for i in range(length_of_number - 2):
            for j in range(i + 1, length_of_number - 1):
                for k in range(j + 1, length_of_number):
                    if int("".join([self.input_str[i], self.input_str[j], self.input_str[k]])) in MULTIPLESOFEIGHT[3]:
                        count += math.pow(2, i) % modulo_var
                        count = count % modulo_var


        final_value = int(count % modulo_var )
        print(final_value)
        return final_value


class TestLuckyNumberEight(unittest.TestCase):
    def test0(self):
        lne = LuckyNumberEight("968")
        self.assertEquals(lne.check_lucky_number_eight(), 3)

    def test1(self):
        lne = LuckyNumberEight("000")
        self.assertEquals(lne.check_lucky_number_eight(), 7)

    def test2(self):
        lne = LuckyNumberEight("00")
        self.assertEquals(lne.check_lucky_number_eight(), 3)

    def test3(self):
        lne = LuckyNumberEight("100")
        self.assertEquals(lne.check_lucky_number_eight(), 3)

    def test4(self):
        lne = LuckyNumberEight("1000")
        self.assertEquals(lne.check_lucky_number_eight(), 8)


if __name__ == "__main__":
    n = int(input().strip())
    arr = input().strip()
    lne = LuckyNumberEight(arr)
    lne.check_lucky_number_eight()
