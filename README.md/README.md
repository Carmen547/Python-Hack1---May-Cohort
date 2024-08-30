Practice of Data Structures and Algorithms
Welcome to the Data Structures and Algorithms Practice repository! The purpose of this project is to implement common algorithms on an advanced level with a particular attention to the exquisiteness of Python. Each solution is not only accurate but optimised for beauty, speed and understandability as well.

TABLE OF CONTENTS
Reverse a String Using a Stack 

Implementing Queue Using Two Stack

Maximum Element In List With In A Linked List

Testing

How to Run the Code

Reverse a String Using a Stack
In this solution, python’s collections.deque is used as the stack to enhance performance of the implementation since all its push and pop operations will be constant time.


from collections import deque

def reverse_string(s: str) -> str:

    stack = deque(s)

    return ''.join([stack.pop() for _ in range(len(stack))])

Implement a Queue Using Two Stacks

This is an interesting implementation of queues using two stacks in such a manner as to hide all the associated logic and enforce the use of the type hints to allow usage of a maintainable and extensible design.

Find the Maximum Element in a List Using a Linked List

This peculiar implementation transforms a linked list into an iterable which allows usage of the max() function contained in Python, thus achieving high efficacy.

Testing

We test our solutions using pytest, which is a testing tool which is both simple and powerful for ensuring the integrity of our solutions. We check for edge cases and make sure that every solution is implemented correctly.

License

This project is free of charge. It is distributed on open source licenses and particularly on MIT License.

By Carmen Kwamboka


