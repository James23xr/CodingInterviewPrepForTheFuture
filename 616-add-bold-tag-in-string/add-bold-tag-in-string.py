class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        n = len(s)
        bold = [False] * n
        for word in words:
            start = s.find(word)
            while start != -1:
                for i in range(start,start+len(word)):
                    bold[i] = True
                start = s.find(word,start+1)
        open_tag = '<b>'
        close_tag = '</b>'
        result_string = []
        for i in range(len(s)):
            if bold[i] and (i==0 or bold[i-1]!=True):
                result_string.append(open_tag)
            result_string.append(s[i])
            if bold[i] and(i==n-1 or bold[i+1]!=True):
                result_string.append(close_tag)
        return ''.join(result_string)
        