def flat(seq):
    if not is_iterable(seq) or isinstance(seq, str):
        yield seq
    else:
        for i in seq:
            yield from flat(i)

def is_iterable(it):
    try:
        _ = iter(it)
    except TypeError:
        return False
    else:
        return True

test = ([1, 'kot'], 3,(4, 5, [7, 8, 9]))
l = list(flat(test))
print(l)
# print([x for x in flat(])
