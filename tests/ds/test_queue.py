from pprint import pprint

from ds.queue import BaseQueue, StandardQueue, DoubleEndsQueue


def test_base_queue():
    queue = BaseQueue(5)
    print(list(queue))

    assert queue.top() is None
    assert queue.dequeue() is None

    for i in range(6):
        queue.enqueue(i)
        print(list(queue))

    assert queue.top().value == 0

    while not queue.is_empty():
        queue.dequeue()
        print(list(queue))


def test_standard_queue():
    queue = StandardQueue(exp2_len=2)
    print(list(queue))

    assert queue.top() is None
    assert queue.dequeue() is None

    print("starting enqueue-ing:\n......")
    queue.enqueue(val={"id": 1, "name": "jack"})
    queue.enqueue(val={"id": 2, "name": "john"})
    queue.enqueue(val={"id": 3, "name": "luis"})
    queue.enqueue(val={"id": 4, "name": "trump"})
    queue.enqueue(val={"id": 5, "name": "elon"})
    print("enqueue finished.\nqueue buffer:")
    pprint(list(queue))

    assert type(queue.top()) is dict

    print("starting dequeue-ing:")
    while not queue.is_empty():
        queue.dequeue()
        print("dequeued: ", list(queue))

    queue2 = StandardQueue(-1)
    queue3 = StandardQueue(2**100)

    assert queue2.size() == 0
    assert queue2.capacity() == 2
    assert queue3.capacity() == 2**10


def test_double_ends_queue():
    assert DoubleEndsQueue(-1).capacity() == 2
    assert DoubleEndsQueue(100).capacity() == 2**10

    queue = DoubleEndsQueue(2)
    assert queue.is_empty() is True
    assert queue.is_full() is False
    assert queue.size() == 0

    queue.push_back("hello")
    queue.push_back("world")
    queue.push_front("hi,")
    queue.push_front("I'm")

    print(list(queue))

    assert queue.push_front("invalid") is False
    assert queue.push_back("invalid") is False

    assert queue.is_full() is True
    assert queue.is_empty() is False

    while not queue.is_empty():
        queue.pop_front()
        queue.pop_back()

    assert queue.pop_back() is None
    assert queue.pop_front() is None

    print(list(queue))
