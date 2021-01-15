class MinStack:
    def __init__(self):
        self.main = []
        self.mins = []
        self.currentMin = float("inf")

    def push(self, x: int) -> None:
        self.main.append(x)
        if x < self.currentMin:
            self.currentMin = x
        self.mins.append(self.currentMin)

    def pop(self) -> None:
        self.main.pop()
        self.mins.pop()
        if len(self.mins) == 0:
            self.currentMin = float("inf")
        elif self.mins[-1] > self.currentMin:
            self.currentMin = self.mins[-1]

    def top(self) -> int:
        return None if len(self.main) == 0 else self.main[-1]

    def getMin(self) -> int:
        return None if len(self.mins) == 0 else self.mins[-1]
