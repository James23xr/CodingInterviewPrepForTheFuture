class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            co = [0] * 26
            for c in s:
                co[ord(c)-ord('a')] += 1
            res[tuple(co)].append(s)
        return res.values()
        