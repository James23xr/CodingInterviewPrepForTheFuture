class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        n = len(s)
        bold = [False] * n
        for word in words:
            start = s.find(word)
            while start !=-1:
                for i in range(start,start+len(word)):
                    bold[i] = True
                start = s.find(word,start+1)
        open_tag = '<b>'
        close_tag = '</b>'
        res = []
        for i in range(len(s)):
            if bold[i] and (i==0 or bold[i-1] !=True):
                res.append(open_tag)
            res.append(s[i])
            if bold[i] and (i==len(s)-1 or bold[i+1]!=True):
                res.append(close_tag)
        return ''.join(res)
        

