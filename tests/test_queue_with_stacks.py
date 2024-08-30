import pytest
from src.queue_with_stacks import QueueWithStacks

def test_queue_with_stacks():
    q = QueueWithStacks()
    q.enqueue(1)
    q.enqueue(2)
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() is None

