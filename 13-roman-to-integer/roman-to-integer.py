class Solution:
    def romanToInt(self, s: str) -> int:
        Map = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        count = 0
        for i in range(len(s)):
            if len(s) == 1:
                return  Map[s[i]]
            elif i == len(s)-1:
                count += Map[s[i]]
            elif Map[s[i]] < Map[s[i+1]]:
                count -= Map[s[i]]
            else:
                count += Map[s[i]]
        return count
            

        