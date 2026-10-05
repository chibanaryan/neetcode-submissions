class MinStack:

    def __init__(self):
        self.stk = []
        self.prefix_min = [float('inf')]

    def push(self, val: int) -> None:
        self.stk.append(val)
        self.prefix_min.append(min(self.prefix_min[-1], val))

    def pop(self) -> None:
        self.stk.pop()
        self.prefix_min.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.prefix_min[-1]
        
