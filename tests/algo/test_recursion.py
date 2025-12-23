from algo.recursion import fib1, fib2, pascal_triangle_recursion, pascal_triangle_iteration


def test_fib():
    for val in fib1(2**10 - 1):
        print(val, end=" ")
    print("\n")
    print(fib2(1))
    print(fib2(20))


def test_pascal_triangle():
    pascal_triangle_recursion(5)
    pascal_triangle_iteration(5)
