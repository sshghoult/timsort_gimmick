def insertion_sort(array: list) -> list:
    """Generic insertion sort of a passed segment; sorts in ascending order"""
    if len(array) < 2:
        return array

    current_pointer = 1
    while current_pointer < len(array):
        placement_pointer = current_pointer - 1
        cur_elem = array[current_pointer]
        while placement_pointer >= 0 and array[placement_pointer] > cur_elem:
            array[placement_pointer], array[placement_pointer + 1] = array[placement_pointer + 1], array[placement_pointer]
            placement_pointer -= 1

        current_pointer += 1

    return array


def merge(x: list, y: list) -> list:
    x_p, y_p = 0, 0
    result = []

    while x_p < len(x) and y_p < len(y):
        if x[x_p] <= y[y_p]:
            result.append(x[x_p])
            x_p += 1
        else:
            result.append(y[y_p])
            y_p += 1

    if x_p < len(x):
        result.extend(x[x_p:])
    elif y_p < len(x):
        result.extend(y[y_p:])

    return result


def collapse_stack(stack: list[list]) -> None:
    """Collapse stack segments to achieve meeting the constraints"""

    if len(stack) < 3:
        return
    # [..., a, b, c]
    a, b, c = stack[-3:]

    while not (len(a) > len(b) + len(c) and len(b) > len(c)):
        if len(a) < len(c):
            merged = merge(a, b)
            stack[-3:-1] = merged
        else:
            merged = merge(b, c)
            stack[-2:] = merged

        if len(stack) < 3:
            return
        a, b, c = stack[-3:]


def final_collapse(stack: list[list]) -> None:
    while len(stack) > 1:
        last = stack.pop()
        prev = stack.pop()

        stack.append(merge(prev, last))


def get_min_run_length(array_length: int) -> int:
    """Mock-function supposedly computing an optimal minimum run-length"""
    ...
    return 4


def get_run(array: list, min_len: int) -> list:
    if len(array) < min_len:
        return array

    slice_barrier = min_len
    while slice_barrier + 1 < len(array) and array[slice_barrier] <= array[slice_barrier + 1]:
        slice_barrier += 1

    return array[:slice_barrier + 1]


def timsort(array: list) -> list:
    """Timsort implementation with some corners cut
    and optimisations ignored for demonstration purposes"""

    merge_stack = []
    minrun_length = get_min_run_length(len(array))
    cur_start = 0
    while cur_start < len(array):
        segment = get_run(array[cur_start:], minrun_length)
        merge_stack.append(insertion_sort(segment))
        cur_start += len(segment)

        collapse_stack(merge_stack)

    final_collapse(merge_stack)

    return merge_stack.pop()
