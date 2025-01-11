class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count_pairs = set()
        for char in s:
            if char in count_pairs:
                count_pairs.remove(char)
            else:
                count_pairs.add(char)
        return len(count_pairs) <= 1
        