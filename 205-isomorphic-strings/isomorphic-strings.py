class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapTS = {}
        mapST = {}
        for i in range(len(s)):
            c1,c2 = s[i],t[i]
            if ((c1 in mapTS and mapTS[c1] != c2) or (c2 in mapST and mapST[c2]!=c1)):
                return False
            mapTS[c1] = c2
            mapST[c2] = c1
        return True
            

        