class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words) < 2:
            return words
        results = []
        for char in set(words[0]):
            count = min(word.count(char) for word in words)
            results += [char]* count
        return results


        
        