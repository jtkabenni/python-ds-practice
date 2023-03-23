def remove_every_other(lst):
    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """

    copy_list = lst.copy()
    copy_list = [num for num in copy_list if copy_list.index(num) % 2 != 1]
    return copy_list
