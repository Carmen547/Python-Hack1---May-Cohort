from typing import Optional

class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next: Optional[Node] = None

class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
    
    def append(self, data: int) -> None:
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)
    
    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next
    
    def find_max(self) -> int:
        if not self.head:
            raise ValueError("The list is empty")
        return max(self)

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(3)
    ll.append(1)
    ll.append(4)
    ll.append(2)
    print(f"Maximum element: {ll.find_max()}")  # Output: 4
