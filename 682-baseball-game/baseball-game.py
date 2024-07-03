class Solution:
    def calPoints(self,ops):
        self.stack = []
        for op in ops:
            if op == "+":
                self.stack.append(self.stack[-1] + self.stack[-2])
            elif op == "D":
                self.stack.append(self.stack[-1] * 2)
            elif op == "C":
                self.stack.pop()
            else:
                self.stack.append(int(op))
        return sum(self.stack)
        