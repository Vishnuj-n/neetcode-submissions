class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.minVal = val
        elif val >= self.minVal:
            self.stack.append(val)
        else:
            self.stack.append(2*val - self.minVal)
            self.minVal = val

    def pop(self) -> None:
        top = self.stack.pop()
        if top < self.minVal:
            self.minVal = 2*self.minVal - top

    def top(self) -> int:
        top = self.stack[-1]
        if top >= self.minVal:
            return top
        return self.minVal

    def getMin(self) -> int:
        return self.minVal