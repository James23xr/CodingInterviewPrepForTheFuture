class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        h_n = {}
        for h,n in zip(heights,names):
            h_n[h] = n
        res = []
        for h in reversed(sorted(heights)):
            res.append(h_n[h])
        return res
        