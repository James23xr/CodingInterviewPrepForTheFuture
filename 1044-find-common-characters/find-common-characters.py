class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words) < 2:
            return words
        first_word = set(words[0])
        letters = []
        for letter in first_word:
            n = min([word.count(letter) for word in words])
            if n:
                letters += [letter]*n
        return letters


        
        