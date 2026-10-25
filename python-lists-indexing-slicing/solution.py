def replace_middle(lst: list, new_items: list) -> None:
    """
    Mutate `lst` in place so that its first and last elements are
    kept and every element between them is replaced by the
    elements of `new_items` (in order). Use slice assignment.
    If `lst` has fewer than 2 elements, do nothing.
    Return nothing.

    Example: lst = [1, 2, 3, 4]; replace_middle(lst, ["x"])
             -> lst is now [1, "x", 4]
    """
    lst1=[]
    if len(lst)<2:
        return None
    else:
        lst1.append(lst[0])
        for i in new_items:
            lst1.append(i)
        lst1.append(lst[-1])
        lst[:]=lst1
        return None
        
    
    pass


def set_every_other(lst: list, value) -> None:
    """
    Mutate `lst` in place so that the elements at positions
    0, 2, 4, ... are all replaced by `value`. Use extended slice
    assignment. Return nothing. An empty list is left empty.

    Example: lst = [1, 2, 3, 4, 5]; set_every_other(lst, 0)
             -> lst is now [0, 2, 0, 4, 0]
    """
    lst[::2] = [value] * len(lst[::2])
    return None
    pass


def slice_copy(lst: list, start: int, stop: int) -> list:
    """
    Return a NEW list containing the elements of `lst` from
    position `start` up to but not including `stop`. Do not
    modify `lst`.
    """
    lst1=lst[start:stop:1]
    return lst1
    pass
