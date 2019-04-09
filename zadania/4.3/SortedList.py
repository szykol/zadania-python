import collections.abc

class SortedList(collections.abc.Sequence):
    def __init__(self, key=lambda a: a):
        self.sequence = []
        self.key = key

    def __getitem__(self, i):
        return self.sequence[i]

    def __len__(self):
        return len(self.sequence)

    def add(self, item):
        index = self._find_index(0, self.__len__() - 1, self.key(item))
        self.sequence.insert(index, item)

    def _find_index(self, l, r, item):

        # if the item is not found - return l which
        # now points to the correct location to insert the item
        if r < l:
            return l
        mid = l + (r - l) // 2

        # get the actual value from the key function
        mid_val = self.key(self.sequence[mid])

        if mid_val > item:
            return self._find_index( l, mid-1, item)
        elif mid_val < item:
            return self._find_index( mid+1, r, item)
        
        # if the item is found - place the item next to it
        return mid + 1

if __name__ == "__main__":
    l = SortedList()
    l.add(1)
    l.add(2)
    l.add(3)
    print(l.sequence)
    l.add(2)
    l.add(7)
    l.add(0)
    print(l.sequence)

    other = SortedList(lambda a: a[1])
    other.add((5, 7))
    other.add((0, 2))
    other.add((0, 1))
    print(other.sequence)