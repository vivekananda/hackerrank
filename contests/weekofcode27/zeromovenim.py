import unittest


# https://www.hackerrank.com/contests/w27/challenges/zero-move-nim

class ZeroMoveNim:
    def __init__(self, heaps):
        self.heaps = heaps

    def can_win(self):

        non_empty_heaps_count = len(filter(lambda x: x != 0, self.heaps))
        if non_empty_heaps_count == 1:
            return True
        if non_empty_heaps_count == 0 :
            return  False

        non_empty_are_odd = non_empty_heaps_count % 2
        xor_value = reduce(lambda x, y: x ^ y, self.heaps)

        can_make_resultant_heapsum_zero = False
        if xor_value != 0:
            if not non_empty_are_odd:
                return True
        else:
            if non_empty_are_odd:
                return True

        return False


class TestZeroMoveNim(unittest.TestCase):
    def test1(self):
        zmn = ZeroMoveNim([1, 2])
        self.assertEquals(zmn.can_win(), True)

    def test2(self):
        zmn = ZeroMoveNim([2, 2])
        self.assertEquals(zmn.can_win(), False)

    def test3(self):
        zmn = ZeroMoveNim([2])
        self.assertEquals(zmn.can_win(), True)


    def test4(self):
        zmn = ZeroMoveNim([])
        self.assertEquals(zmn.can_win(), False)


if __name__ == "__main__":
    number_of_games = int(raw_input().strip())
    for i in range(number_of_games):
        number_of_heaps = int(raw_input().strip())
        heaps = map(int, raw_input().strip().split())
        zmn = ZeroMoveNim(heaps)
        if zmn.can_win():
            print("W")
        else:
            print("L")
