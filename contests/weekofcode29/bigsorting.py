import unittest


# Catch is for int in python there are no limits :)

class BigSorting():
    pass

class TestBigSorting(unittest.TestCase):

    def test1(self):
        pass


if __name__ == "__main__":
    n = int(input().strip())
    arr = []
    for i in range(n):
        arr.append(int(input().strip()))
    arr.sort()
    for el in arr:
        print(el)

