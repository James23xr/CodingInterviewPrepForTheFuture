class Solution:
    def isValid(self, s: str) -> bool:
        has = {"}":"{",")":"(","]":"["}
        stack = []
        for char in s:
            if len(s) <=1:
                return False
            if char in has:
                if stack and has[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0

        