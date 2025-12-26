import pytest

from ds.examples.stack_example import valid_brackets, rpn, infix_to_suffix
from ds.stack import LinkedStack, StandardStack


def test_linked_queue():
    stack = LinkedStack(6)
    print(list(stack))

    assert stack.size() == 0
    assert stack.capacity() == 6
    assert stack.top() is None
    assert stack.pop() is None

    print("start pushing:")
    for i in range(100):
        stack.push(i)
        if not stack.is_full():
            print(list(stack))

    assert stack.top().value == 5

    print("stack:")
    print(list(stack))
    print("start poping:")

    while not stack.is_empty():
        print(f"pop-ed: {stack.pop()}, remains", list(stack))
    print(list(stack))


def test_standard_stack():
    stack = StandardStack(6)
    print(list(stack))

    assert stack.size() == 0
    assert stack.capacity() == 6
    assert stack.top() is None
    assert stack.pop() is None

    print("start pushing:")
    for i in range(100):
        stack.push(i)
        if not stack.is_full():
            print(list(stack))

    assert stack.top() == 5

    print("stack:")
    print(list(stack))
    print("start poping:")

    while not stack.is_empty():
        print(f"pop-ed: {stack.pop()}, remains", list(stack))
    print(list(stack))


def test_brackets():
    assert valid_brackets("{()}<>[](())") is True
    assert valid_brackets("[][[[}}}") is False


def test_rpn():
    with pytest.raises(ValueError):
        rpn("1,2,+,")
    print(rpn("1,2,+,-4,abs,+,5,square,+"))
    # (1 + 2) + abs(-4) + 5**2 = 3 + 4 + 25 = 7 + 25 = 32
    with pytest.raises(Exception):
        rpn("1,2,+,-4,abs,5,square")
    # (1 + 2) abs(-4) 5**2
    # 没有符号连起来，最后只弹出了 5**2 = 25
    assert rpn("1,2,3,*,+") == 7


def test_infix_to_suffix():
    assert infix_to_suffix("1+2") == "1,2,+"
    assert infix_to_suffix("1+2-3") == "1,2,+,3,-"
    assert infix_to_suffix("1+2*3") == "1,2,3,*,+"
    assert infix_to_suffix("1*2-3") == "1,2,*,3,-"
    assert infix_to_suffix("(1+2)*3") == "1,2,+,3,*"
    assert infix_to_suffix("1+2*3+(4*5+6)*7") == "1,2,3,*,+,4,5,*,6,+,7,*,+"
    with pytest.raises(Exception):
        infix_to_suffix("1++2")
