from typing import List

class QueueWithStacks:
    def __init__(self):
        self._stack_in: List[int] = []
        self._stack_out: List[int] = []
    
    def enqueue(self, x: int) -> None:
        self._stack_in.append(x)
    
    def _transfer(self) -> None:
        while self._stack_in:
            self._stack_out.append(self._stack_in.pop())
    
    def dequeue(self) -> int:
        if not self._stack_out:
            self._transfer()
        return self._stack_out.pop() if self._stack_out else None

if __name__ == "__main__":
    q = QueueWithStacks()
    q.enqueue(1)
    q.enqueue(2)
    print(f"Dequeued element: {q.dequeue()}")  # Output: 1
    print(f"Dequeued element: {q.dequeue()}")  # Output: 2
