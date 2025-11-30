class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)
        for window_start in range(m-n+1):
            for i in range(n):
                if needle[i] != haystack[window_start+i]:
                    break
                if i == n-1:
                    return window_start
        return -1

        