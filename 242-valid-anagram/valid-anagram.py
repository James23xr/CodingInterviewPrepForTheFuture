class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0] *26
        for ch in s:
            i = ord(ch)-ord('a')
            count[i] +=1
        for ch in t:
            i = ord(ch)-ord('a')
            count[i] -=1
            if count[i] <0:
                return False
        return True
        