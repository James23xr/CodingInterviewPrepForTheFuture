class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = {}
        char_index = {}
        
        for i, char in enumerate(s):
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
                char_index[char] = i
        
        min_index = float('inf')
        for char, count in char_count.items():
            if count == 1:
                min_index = min(min_index, char_index[char])
        
        return min_index if min_index != float('inf') else -1