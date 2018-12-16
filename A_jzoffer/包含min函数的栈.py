用一个辅助栈来存最小值

class Solution:
    def __init__(self):
        self.stack = []
        self.minstack = []
    def push(self, node):
        # write code here
        if not self.minstack or self.minstack[-1] >= node:
            self.minstack.append(node)
        self.stack.append(node)
    def pop(self):
        # write code here
        if self.minstack[-1] == self.stack[-1]:
            self.minstack.pop()
        self.stack.pop()
    def top(self):
        # write code here
        if self.stack:
            return self.stack[-1]
    def min(self):
        # write code here
        if self.minstack:
            return self.minstack[-1]