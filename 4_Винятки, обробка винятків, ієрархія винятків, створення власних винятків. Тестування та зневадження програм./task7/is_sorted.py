def is_sorted(lst):
    """
    (list) -> (bool)
    The function returns True if the list is sorted and False if not
    """
    if isinstance(lst, list):
        if len(lst) == 0:
            return False
        for i in lst:
            if not isinstance(i, int):
                return False
        if sorted(lst) == lst:
            return True
        return False
    return False
