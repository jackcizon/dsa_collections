from typing import Iterator


def fib1(limit: int) -> Iterator[int]:
    """value control, given a limit"""
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


def fib2(times: int) -> int:
    """frequency control"""
    if times < 2:
        return times
    a, b = 0, 1
    for _ in range(2, times + 1):
        a, b = b, a + b
    return b


def pascal_triangle_recursion(rows: int) -> None:
    """Recursion is better suited for describing problems,
    while iteration is better suited for executing problems."""
    for row in range(rows):
        for col in range(row + 1):
            print(_pascal_triangle_element_recursion(row, col), end=" ")
        print("\n")


def _pascal_triangle_element_recursion(row: int, col: int) -> int:
    """return triangle element recursively"""
    if row == col or col == 0:
        return 1
    return _pascal_triangle_element_recursion(row - 1, col) + _pascal_triangle_element_recursion(
        row - 1, col - 1
    )


def pascal_triangle_iteration(rows: int) -> None:
    prev: list[int] = []
    for _ in range(rows):
        curr = [1] * (len(prev) + 1)
        for i in range(1, len(prev)):
            curr[i] = prev[i - 1] + prev[i]
        print(*curr)
        prev = curr
