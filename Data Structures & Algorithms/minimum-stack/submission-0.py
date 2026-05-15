class MinStack:

    def __init__(self):
        self.ints = []
        self.min = []

    def push(self, val: int) -> None:
        self.ints.append(val)
        if self.min:
            val = min(val, self.min[-1])
        self.min.append(val)

    def pop(self) -> None:
        self.ints.pop()
        self.min.pop()

    def top(self) -> int:
        return self.ints[-1]

    def getMin(self) -> int:
        return self.min[-1]
