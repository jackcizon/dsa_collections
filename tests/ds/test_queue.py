from pprint import pprint

from ds.queue import BaseQueue, StandardQueue


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
    queue3 = StandardQueue(2 ** 100)

    assert queue2.size() == 0
    assert queue2.capacity() == 2
    assert queue3.capacity() == 2 ** 10
