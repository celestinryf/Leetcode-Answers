class MinStack:

    def __init__(self):
        self.min = float('inf')
        self.stack = []

    def push(self, theValue: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = theValue
        else:
            self.stack.append(theValue - self.min)
            if theValue < self.min:
                self.min = theValue

    def pop(self) -> None:
        if not self.stack:
            return

        pop = self.stack.pop()

        if pop < 0:
            self.min = self.min - pop

    def top(self) -> int:
        top = self.stack[-1]
        if top > 0:
            return top + self.min
        else:
            return self.min

    def getMin(self) -> int:
        return self.min

