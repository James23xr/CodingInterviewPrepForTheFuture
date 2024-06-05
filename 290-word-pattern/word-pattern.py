class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        CharToWord = {}
        WordToChar = {}
        if len(pattern) != len(words):
            return False
        for c,w in zip(pattern,words):
            if c in CharToWord and CharToWord[c] != w:
                return False
            if w in WordToChar and WordToChar[w] != c:
                return False
            CharToWord[c] = w
            WordToChar[w] = c
        return True

        

        