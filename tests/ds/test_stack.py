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
