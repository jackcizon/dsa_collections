from pprint import pprint

from ds.queue import (
    BaseQueue,
    StandardQueue,
    DoubleEndsQueue,
    UnorderedArrayPriorityQueue,
    OrderArrayPriorityQueue,
    PriorityQueue,
)


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


def test_array_pq():
    pq1 = UnorderedArrayPriorityQueue(2)

    assert pq1.is_empty() is True
    assert pq1.dequeue() is None
    assert pq1.top() is None

    i = 0
    while not pq1.is_full():
        pq1.enqueue(i)
        i += 1
    pq1.enqueue(100)
    print(list(pq1))

    assert pq1.top() == 1
    assert pq1.is_full() is True
    assert pq1.dequeue() == 1
    assert pq1.dequeue() == 0

    pq1 = OrderArrayPriorityQueue(2)

    assert pq1.is_empty() is True
    assert pq1.dequeue() is None
    assert pq1.top() is None

    i = 1
    while not pq1.is_full():
        pq1.enqueue(i)
        i -= 1
    pq1.enqueue(100)
    print(list(pq1))

    assert pq1.top() == 1
    assert pq1.is_full() is True
    assert pq1.dequeue() == 1
    assert pq1.dequeue() == 0


def test_max_heap():
    pq = PriorityQueue(capacity=10)

    assert pq.top() is None

    # 测试 push
    print("=== Push ===")
    for val in [5, 3, 8, 1, 6]:
        pq.enqueue(val)

    print(list(pq))

    # 测试 top
    print("\n=== Top ===")
    print(f"Current top: {pq.top()}")  # 应该是 8

    # 测试 pop
    print("\n=== Pop ===")
    while not pq.is_empty():
        pq.dequeue()

    # 测试 pop 空堆
    print("\n=== Pop empty ===")
    print(pq.dequeue())  # None

    # 测试 push 到满堆
    print("\n=== Push to full ===")
    for val in range(1, 12):
        pq.enqueue(val)

    # 检查 top
    print("\n=== Final Top ===")
    print(pq.top())  # 应该是 10
