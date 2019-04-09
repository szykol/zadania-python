import unittest
from SortedList import SortedList

class TestSortedList(unittest.TestCase):
    def test_empty_at_first(self):
        # Test if the SortedList is empty at the start
        self.assertEqual(len(SortedList()), 0)

    def test_correct_len(self):
        # Test if object has correct length
        sl = SortedList()
        sl.add(10)
        self.assertEqual(len(sl), 1)

        sl.add(0)
        sl.add(15)
        self.assertEqual(len(sl), 3)

    def test_getitem(self):
        # Test if __getitem__ is correctly implemented
        sl = SortedList()

        items = [(0, 1), (0, 2), (0, 3)]
        for item in items:
            sl.add(item)

        # Test if indices work correctly aswell as reversed
        for i, ri in zip(range(len(sl)), reversed(range(len(sl)))):
            self.assertEqual(items[i], sl[i])
            self.assertEqual(items[ri], sl[ri])

        with self.assertRaises(IndexError):
            sl[10]

    def test_accepts_duplicates(self):
        # Test if object accepts duplicate items
        sl = SortedList()
        sl.add(0)
        sl.add(0)

        self.assertEqual(len(sl), 2)
        
    def test_correct_order(self):
        # Test if object puts items in correct order
        items = [5, 3, 10, 1, 15, 20, 30]

        sl = SortedList()
        for item in items:
            sl.add(item)

        self.assertEqual(sorted(items), sl.sequence)

    def test_specified_key(self):
        # Test if object inserts values in correct order
        # if the key is specified
        key_1 = lambda a: a[0]
        key_2 = lambda a: a[1]

        sl_key1 = SortedList(key_1)
        sl_key2 = SortedList(key_2)

        items = [(0, 1), (-5, 29), (1, 15), (-3, 29)]
        for item in items:
            sl_key1.add(item)
            sl_key2.add(item)

        self.assertEqual(sorted(items, key=key_1), sl_key1.sequence)
        self.assertEqual(sorted(items, key=key_2), sl_key2.sequence)
