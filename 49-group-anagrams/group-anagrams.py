from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word))
            groups[key].append(word)
        return list(groups.values())
        