import unittest
from SortedList import SortedList

class TestSortedList(unittest.TestCase):
    def test_empty_at_first(self):
        """ Test if the SortedList is empty at the start """
        self.assertEqual(len(SortedList()), 0)

    def test_add(self):
        sl = SortedList()
        sl.add(1)

        self.assertEqual(sl.sequence, [1])

    def test_correct_order(self):
        """ Test if object puts items in correct order """
        items = [5, 3, 10, 1, 15, 20, 30]

        sl = SortedList()
        for item in items:
            sl.add(item)

        self.assertEqual(sorted(items), sl.sequence)

    def test_correct_len(self):
        """ Test if object has correct length """
        sl = SortedList()
        sl.add(10)
        self.assertEqual(len(sl), 1)

        sl.add(0)
        sl.add(15)
        self.assertEqual(len(sl), 3)

    def test_getitem(self):
        """ Test if __getitem__ is correctly implemented """
        sl = SortedList()

        items = [(0, 1), (0, 2), (0, 3)]
        for item in items:
            sl.add(item)

        # Test if indices work correctly aswell as reversed
        for i, ri in zip(range(len(sl)), reversed(range(len(sl)))):
            self.assertEqual(items[i], sl[i])
            self.assertEqual(items[ri], sl[ri])

        self.assertRaises(IndexError, sl.__getitem__, 10)

    def test_accepts_duplicates(self):
        """ Test if object accepts duplicate items """
        sl = SortedList()
        sl.add(0)
        sl.add(0)

        self.assertEqual(len(sl), 2)

    def test_specified_key(self):
        """ Test if object inserts values in correct order
            if the key is specified """
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

    def test_extend(self):
        """ Test if object accepts an iterable
            and puts all of it's items in correct
            order """
        sl = SortedList()

        items = [3, 0, 1, 15]
        sl.extend(items)
        self.assertEqual(sorted(items), sl.sequence)

        more_items = [-5, 20, 3]
        sl.extend(more_items)
        self.assertEqual(sorted(items + more_items), sl.sequence)
        sl.extend([])
        self.assertEqual(sorted(items + more_items), sl.sequence)

    def test_pop(self):
        """ Test if the object pops correctly """
        sl = SortedList()

        with self.assertRaises(IndexError):
            sl.pop()
            sl.pop(0)

        sl.add(5)
        self.assertEqual(sl.pop(), 5)

        sl.extend([6,90,3,4,9])

        self.assertEqual(sl.pop(), 90)
        self.assertEqual(sl.pop(0), 3)
        self.assertEqual(sl.sequence, [4, 6, 9])
        
    def test_clear(self):
        """ Test if object clears it's contents """
        sl = SortedList()
        sl.extend([0, 10, 20, -5, -200])
        
        sl.clear()
        self.assertEqual(len(sl), 0)
        self.assertEqual(sl.sequence, [])

    def test_remove(self):
        """ Test if object removes items """
        sl = SortedList()
        sl.extend([0, 10, 20, -5, 10])

        sl.remove(0)
        self.assertEqual(sl.sequence, [-5, 10, 10, 20])

        sl.remove(10)
        self.assertEqual(sl.sequence, [-5, 10, 20])
        sl.remove(10)
        self.assertEqual(sl.sequence, [-5, 20])

        self.assertRaises(ValueError, sl.remove, 10)

    def test_count(self):
        """ Test if returns correct count of an item """
        sl = SortedList()
        sl.extend([0, 4, 3, 4, 3, 4, 10, 4, 10, 3])

        self.assertEqual(sl.count(4), 4)
        self.assertEqual(sl.count(3), 3)
        self.assertEqual(sl.count(0), 1)
        self.assertEqual(sl.count(2000), 0)
        
    def test_copy(self):
        """ Test if returns a copy of it's contents """
        sl = SortedList()

        self.assertEqual(sl.copy(), [])

        sl.extend([10, 5, 20, 3])
        self.assertEqual(sl.copy(), [3, 5, 10, 20])

    def test_index(self):
        """ Test if returns the index of an item """
        sl = SortedList()
        self.assertRaises(ValueError, sl.index, 0) 

        sl.extend([0, 1, 1, 10, 1, 15, 20])
        self.assertEqual(sl.index(0), 0)
        self.assertEqual(sl.index(1), 1)

        self.assertEqual(sl.index(1, 3), 3)
        self.assertRaises(ValueError, sl.index, 10, 0, 3) 


