import random


def time(fun, arr):
    """
    `time(fun, arr)` takes a sort `fun` and an array `arr` as input, and returns the sort name,
    the time it took to run the sort, and the output of the sort.

    :param fun: the sort to be timed
    :param arr: the array to be sorted
    :return: The sort name, the time it took to run, and the output of the sort.
    """
    import time
    start = time.time()
    out = fun(arr)
    end = time.time()
    simtime = round((end - start) * 1000, 4)
    print(fun.__name__, simtime, "ms", out)
    return fun.__name__, simtime, out


if __name__ == '__main__':
    import sorts
    arrayOfSorts = [
        sorts.gnome,
        sorts.quick,
        sorts.insertion,
        sorts.bubble,
        sorts.merge,
        sorts.selection,
        sorts.selection2x
    ]
    # prep test array
    test = []
    for i in range(100):
        test.append(random.randint(0, 10))
    # run tests
    for sort in arrayOfSorts:
        breakableTest = test.copy()
        time(sort, breakableTest)
