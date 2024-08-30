from collections import deque

def reverse_string(s: str) -> str:
    stack = deque(s)
    return ''.join(stack.pop() for _ in range(len(stack)))

if __name__ == "__main__":
    sample_input = "hello"
    print(f"Reversed string: {reverse_string(sample_input)}")  # Output: "olleh"
