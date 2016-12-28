import unittest


# https://www.hackerrank.com/challenges/candies
class Candies:
    def __init__(self, n=None, ratings=None):
        if n is None:
            self.n = int(input().strip())
            self.ratings = []
            for i in range(self.n):
                self.ratings.append(int(input().strip()))
        else:
            self.n = n
            self.ratings = ratings

    def total_candies(self):
        candies = [1] * self.n
        for i in range(1, self.n):
            if self.ratings[i] > self.ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        for i in range(self.n - 2, -1, -1):
            if self.ratings[i] > self.ratings[i + 1] and candies[i] < candies[i + 1] + 1:
                candies[i] = candies[i + 1] + 1
        # print(self.ratings)
        # print(candies)
        return sum(candies)


class TestCandies(unittest.TestCase):
    def test1(self):
        c = Candies(3, [2, 2, 1])
        self.assertEquals(c.total_candies(), 4)

    def test2(self):
        c = Candies(5, range(5))
        self.assertEquals(c.total_candies(), 15)

    def test3(self):
        c = Candies(5, range(5, 0, -1))
        self.assertEquals(c.total_candies(), 15)

    def test4(self):
        c = Candies(10, range(5) + range(5, 0, -1))
        self.assertEquals(c.total_candies(), 31)

    def test5(self):
        c = Candies(1, [1])
        self.assertEquals(c.total_candies(), 1)


if __name__ == "__main__":
    c = Candies()
    print(c.total_candies())
