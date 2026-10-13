class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0] * 26
        for char in s:
            i = ord(char) - ord('a')
            count[i] +=1
        for char in t:
            i = ord(char) - ord('a')
            count[i] -=1
        for char in count:
            if char != 0:
                return False
        return True
        