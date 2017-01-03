import unittest

# https://www.hackerrank.com/challenges/xor-se

class XorSequence:
    def __init__(self,L=None,R=None):
        if L is None:
            self.L,self.R = map(int, input().strip().split(" "))
        else:
            self.L = L
            self.R = R
    def get_element_at_i(self,i):
        r = i % 4
        v = 0
        if r == 0 :
            v = i
        elif r == 1:
            v = 1
        elif r == 2:
            v = i + 1
        elif r == 3:
            v = 0
        #print(v)
        return v

    def range_calculae(self,left,right):
        #print ("range",left, right)
        txors = self.get_element_at_i(left)
        for i in range(left + 1, right + 1):
            txors ^= self.get_element_at_i(i)
        return txors

    def calculate(self):
        diff = int(self.R/4) - int(self.L/4)
        if diff >= 2:
            # left sum
            left_sum = self.range_calculae(self.L,(int(self.L/4)+1)*4-1)
            # mid sum
            mid_sum = 0
            if diff % 2 == 0:
                mid_sum = 2
            # right sum
            right_sum = self.range_calculae(int(self.R/4)*4,self.R)
            #print(left_sum, mid_sum, right_sum)
            return  left_sum ^ mid_sum ^ right_sum
        else:
            return self.range_calculae(self.L,self.R)




class TestXorSequence(unittest.TestCase):
    def test1(self):
        xors = XorSequence(2,4)
        self.assertEquals(xors.calculate(),7)


    def test2(self):
        xors = XorSequence(2, 8)
        self.assertEquals(xors.calculate(), 9)


    def test3(self):
        xors = XorSequence(5,9)
        self.assertEquals(xors.calculate(), 15)


if __name__ == "__main__":
    n = int(input().strip())
    for i in range(n):
        xors = XorSequence()
        print(xors.calculate())
