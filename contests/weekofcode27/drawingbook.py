import unittest
import math


# https://www.hackerrank.com/contests/w27/challenges/drawing-book

class DrawingBook:
    def __init__(self, n, p):
        self.n = self._get_next_odd(n)
        self.p = self._get_next_odd(p)

    def _get_next_odd(self, x):
        if x % 2:
            return x
        else:
            return x + 1

    def calculate(self):
        from_left = self.p / 2
        from_right = (self.n - self.p) / 2
        if from_left < from_right:
            return math.floor(from_left)
        else:
            return math.floor(from_right)


class TestDrawingBook(unittest.TestCase):
    def test1(self):
        db = DrawingBook(6, 2)
        self.assertEquals(db.calculate(), 1)

    def test2(self):
        db = DrawingBook(5, 4)
        self.assertEquals(db.calculate(), 0)


if __name__ == "__main__":
    n = int(input().strip())
    p = int(input().strip())

    db = DrawingBook(n, p)
    print(db.calculate())
