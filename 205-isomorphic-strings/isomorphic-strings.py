class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapTS = {}
        mapST = {}
        for c1,c2 in zip(s,t):
            if ((c1 in mapTS and mapTS[c1] != c2) or (c2 in mapST and mapST[c2]!=c1)):
                return False
            mapTS[c1] = c2
            mapST[c2] = c1
        return True
            

        