import unittest
import math

# https://www.hackerrank.com/challenges/30-running-time-and-complexity

class RunningTimeComplexity:
    def __init__(self, data):
        self.data = data

    def check_print_prime(self):
        self.check_prime()

    def check_prime(self):
        prime = True
        if self.data == 1:
            prime = False
        elif self.data == 2:
            prime = True
        elif self.data % 2 == 0:
            prime = False
        else:
            for i in range(3, math.ceil(math.sqrt(self.data)) + 2, 2):
                if self.data != i and self.data % i == 0:
                    prime = False
                    break

        if prime:
            print("Prime")
        else:
            print("Not prime")
        return prime


class TestRunningTimeComplexity(unittest.TestCase):
    def test0(self):
        rtc = RunningTimeComplexity(2)
        self.assertEquals(rtc.check_prime(), True)

        rtc = RunningTimeComplexity(3)
        self.assertEquals(rtc.check_prime(), True)

    def test1(self):
        rtc = RunningTimeComplexity(12)
        self.assertEquals(rtc.check_prime(), False)

    def test2(self):
        rtc = RunningTimeComplexity(5)
        self.assertEquals(rtc.check_prime(), True)

    def test3(self):
        rtc = RunningTimeComplexity(7)
        self.assertEquals(rtc.check_prime(), True)

    def test4(self):
        rtc = RunningTimeComplexity(25)
        self.assertEquals(rtc.check_prime(), False)

    def test5(self):
        rtc = RunningTimeComplexity(7919)
        self.assertEquals(rtc.check_prime(), True)

    def test6(self):
        rtc = RunningTimeComplexity(179426549)
        self.assertEquals(rtc.check_prime(), True)

    def test7(self):
        rtc = RunningTimeComplexity(1000000007)
        self.assertEquals(rtc.check_prime(), True)

    def test8(self):
        rtc = RunningTimeComplexity(100000003)
        self.assertEquals(rtc.check_prime(), False)

    def test9(self):
        rtc = RunningTimeComplexity(1000003)
        self.assertEquals(rtc.check_prime(), True)


if __name__ == "__main__":
    no_of_data_points = int(input().strip())
    for i in range(no_of_data_points):
        data = int(input().strip())
        rtc = RunningTimeComplexity(data)
        rtc.check_prime()
