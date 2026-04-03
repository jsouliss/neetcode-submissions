class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.appendleft(x)

    def pop(self) -> int:
        curr = self.q.popleft()
        return curr

    def top(self) -> int:
        curr = self.q[0]
        return curr

    def empty(self) -> bool:
        if self.q:
            return False
        return True

        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()