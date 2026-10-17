class MinStack:
    def __init__(self):
        self.stacka = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stacka.append(val)
        if not self.minstack:
            self.minstack.append(val)
        elif (val > self.minstack[-1]):
            self.minstack.append(self.minstack[-1])
        else:
            self.minstack.append(val)

    def pop(self) -> None:
        del self.stacka[-1]
        del self.minstack[-1]

    def top(self) -> int:
        return self.stacka[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
        
