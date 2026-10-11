from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)
        for word in strs:
            count = [0] *26
            for char in word:
                i = ord(char)-ord('a')
                count[i] +=1
            groups[tuple(count)].append(word)
        return list(groups.values())
        