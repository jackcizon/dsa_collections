from ds.queue import BaseQueue


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
