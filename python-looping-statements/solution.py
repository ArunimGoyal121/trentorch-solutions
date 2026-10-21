def countdown_with_skip(start: int) -> list:
    """
    Using a while loop, count down from `start` to 1 (inclusive),
    appending each number to a list, but skip appending any
    number that is exactly 3 (use continue for this).
    Do not use break here.
    Return the resulting list.
    """
    result = []
    current = start
    while current >= 1:
        if current == 3:
            current -= 1
            continue
        result.append(current)
        current -= 1
    return result
    pass


def find_first_negative(numbers: list) -> int | None:
    """
    Using a while loop with an index variable, find and return
    the first negative number in `numbers`. Use break once found.
    If no negative number exists, use the loop's else clause to
    return None after the loop completes normally.
    """
    count=0
    for i in numbers:
        if i<0:
            return i
            count=1
            break
    if count!=1:
        return None

    pass


def sum_with_index(numbers: list) -> dict:
    """
    Using a for loop with enumerate(), build and return a
    dictionary mapping each index to the running sum of all
    numbers up to and including that index.

    Example: sum_with_index([10, 20, 30])
    -> {0: 10, 1: 30, 2: 60}
    """
    d={}
    sum=0
    no=0
    for i in numbers:
        sum=sum+i
        d[no]=sum
        no+=1
    return d
    pass


def manual_iteration_trace(items: list) -> list:
    """
    Without using a for loop, replicate what a for loop does
    internally: use iter() to get an iterator from `items`, then
    repeatedly call next() on it inside a while loop, catching
    StopIteration to know when to stop.

    Return a list of all elements retrieved this way, in order
    (it should exactly match the original `items` list).
    """
    result = []
    iterator = iter(items)
    while True:
        try:
            result.append(next(iterator))
        except StopIteration:
            break
    return result
    pass
