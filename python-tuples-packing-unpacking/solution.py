def rotate_three(a, b, c) -> tuple:
    """
    Return a tuple (b, c, a): the three values rotated one
    position to the left. Do this using a single multiple
    assignment statement `a, b, c = b, c, a` and then return
    a packed tuple of the three variables.

    Example: rotate_three(1, 2, 3) -> (2, 3, 1)
    """
    t=b,c,a
    return t
    pass


def head_and_tail(seq) -> tuple:
    """
    `seq` is any sequence (list, tuple, or string). Using
    extended unpacking, return a 2-element tuple (head, tail)
    where `head` is the first element and `tail` is a LIST of
    all remaining elements.

    If `seq` is empty, return (None, []).

    Example: head_and_tail((1, 2, 3)) -> (1, [2, 3])
    """
    if not seq:
        return None , []
    first , *rest=seq
    t=first,rest
    return t
    pass


def ends_and_middle(seq) -> tuple:
    """
    `seq` has at least 2 elements. Using extended unpacking,
    return a 3-element tuple (first, middle, last) where
    `middle` is a LIST of the elements between them (empty if
    there are none).

    Example: ends_and_middle([1, 2, 3, 4]) -> (1, [2, 3], 4)
             ends_and_middle("ab")         -> ("a", [], "b")
    """
    first , *mid, last=seq
    return first,mid,last
    pass


def sum_pairs(pairs: list) -> list:
    """
    `pairs` is a list of 2-element tuples of numbers. Return a
    new list where each element is the sum of the matching
    pair. Unpack each pair into two loop variables.

    Example: sum_pairs([(1, 2), (3, 4)]) -> [3, 7]
    """
    l=[]
    for i in pairs:
        sum=0
        for j in i:
            sum+=j
        l.append(sum)
    return l

    
    pass
