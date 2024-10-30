class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS = defaultdict(int)
        countT = defaultdict(int)
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)
        for char in s:
            if countS[char] != countT.get(char,0):
                return False
        return True