class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False

        charToWord = {} 
        WordToChar = {}

        for c,w in zip(pattern, words):
            if c in charToWord and charToWord[c] != w:
                return False
            if w in WordToChar and WordToChar[w] != c:
                return False
            charToWord[c] = w
            WordToChar[w] = c
        return True

        

        