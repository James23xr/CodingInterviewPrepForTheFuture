class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        Map = {"}":"{","]":"[",")":"("}
        for char in s:
            if len(s) <= 1:
                return False
            if char in Map:
                if stack and stack[-1] == Map[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0
        