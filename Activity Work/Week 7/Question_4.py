class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val < self.min_stack:
            self.min_stack = val

    def pop(self) -> None:
        if self.stack:
            if self.stack[-1] == self.min_stack:
                self.min_stack = min(self.stack[:-1]) if len(self.stack) > 1 else None
            
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
            
        return None

    def getMin(self) -> int:
        return self.min_stack

# Example usage:
if __name__ == "__main__":
    min_stack = MinStack()
    print(min_stack.push(-2))
    print(min_stack.push(0))
    print(min_stack.push(-3))
    print(min_stack.getMin()) 
    print(min_stack.pop())
    print(min_stack.top())
    print(min_stack.getMin())
