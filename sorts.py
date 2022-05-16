def gnome(a):
    """
    "If the current element is greater than or equal to the previous element, move to the next element.
    Otherwise, swap the current element with the previous element and move to the previous element."

    The function is called gnome because it's a reference to the Gnome Sort algorithm

    :param a: the list to be sorted
    :return: The sorted list.
    """
    i = 0
    while i < len(a):
        if i == 0 or a[i] >= a[i - 1]:
            i += 1
        else:
            a[i], a[i - 1] = a[i - 1], a[i]
            i -= 1
    return a


def quick(a):
    """
    If the list is empty or has one element, return the list. Otherwise, pick the first element as the
    pivot, partition the rest of the list into two lists, one with elements less than the pivot and one
    with elements greater than the pivot, and return the concatenation of the sorted left list, the
    pivot, and the sorted right list

    :param a: the list to be sorted
    :return: the sorted list.
    """
    if len(a) <= 1:
        return a
    else:
        pivot = a[0]
        left = []
        right = []
        for i in range(1, len(a)):
            if a[i] < pivot:
                left.append(a[i])
            else:
                right.append(a[i])
        return quick(left) + [pivot] + quick(right)


def insertion(a):
    """
    Starting at the second element, if the element is less than the previous element, swap them, and
    repeat until the element is greater than or equal to the previous element.

    :param a: the list to be sorted
    :return: The sorted list.
    """
    for i in range(1, len(a)):
        j = i
        while j > 0 and a[j] < a[j - 1]:
            a[j], a[j - 1] = a[j - 1], a[j]
            j -= 1
    return a


def bubble(a):
    """
    "For each element in the list, compare it to the next element and swap them if the first element is
    greater than the second element."

    The bubble sort algorithm is not very efficient. It has a time complexity of O(n^2)

    :param a: the list to be sorted
    :return: The sorted list.
    """
    for i in range(0, len(a)):
        for j in range(0, len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a
# comb and merge are a pair


def comb(a, b):
    """
    "If the list is empty or has one element, return it; otherwise, split the list in half, sort each
    half, and merge the two sorted halves."

    The function is recursive, so it calls itself. The base case is when the list has zero or one
    elements. In that case, the list is already sorted, so we return it. Otherwise, we split the list in
    half, sort each half, and merge the two sorted halves

    :param a: the list to be sorted
    :param b: the list to be sorted
    :return: The sorted list.
    """
    c = []
    while a and b:
        if a[0] <= b[0]:
            c.append(a.pop(0))
        else:
            c.append(b.pop(0))
    if a:
        c.extend(a)
    if b:
        c.extend(b)
    return c


def merge(a):
    if len(a) <= 1:
        return a
    else:
        mid = len(a) // 2
        return comb(merge(a[:mid]), merge(a[mid:]))


def selection(a):
    """
    For each element in the array, find the index of the smallest element to the right of the current
    element, and swap the current element with the smallest element to the right of the current element

    :param a: the list to be sorted
    :return: The sorted array
    """
    for i in range(len(a)):
        minIndex = i
        for j in range(i, len(a)):
            if a[j] < a[minIndex]:
                minIndex = j
        a[i], a[minIndex] = a[minIndex], a[i]
    return a


def selection2x(a):
    """
    It takes an array of numbers, and returns an array of the same numbers, but with the smallest number
    first, the largest number second, the second smallest number third, the second largest number
    fourth, and so on

    :param a: the list to be sorted
    :return: a list of the elements of the input list in ascending order.
    """
    minFirst = []
    maxFirst = []
    minIndex = 0
    maxIndex = 0
    while (True):
        for i in range(0, len(a)):
            if a[i] < a[minIndex]:
                minIndex = i
            if a[i] > a[maxIndex]:
                maxIndex = i
        if (len(a) == 0):
            break
        elif (len(a) == 1):
            maxFirst.insert(0, a.pop(minIndex))
            break
        elif (minIndex < maxIndex):
            minFirst.append(a.pop(minIndex))
            maxFirst.insert(0, a.pop(maxIndex - 1))
        elif (minIndex > maxIndex):
            maxFirst.insert(0, a.pop(maxIndex))
            minFirst.append(a.pop(minIndex - 1))
        else:
            for av in a:
                minFirst.append(av)
            break
        minIndex = 0
        maxIndex = 0
    return minFirst + maxFirst
