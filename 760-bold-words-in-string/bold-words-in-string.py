class Solution:
    def boldWords(self, words: List[str], s: str) -> str:
        if not words:
            return s
        if not s:
            return None
        n = len(s)
        bold = [False]*n
        for word in words:
            start = s.find(word)
            while start != -1:
                for i in range(start,start+len(word)):
                    bold[i] = True
                start =s.find(word,start+1)
        open_tag = '<b>'
        close_tag = '</b>'
        res = []
        for i in range(n):
            if bold[i] and (i==0 or not bold[i-1]):
                res.append(open_tag)
            res.append(s[i])
            if bold[i] and (i==n-1 or not bold[i+1]):
                res.append(close_tag)
        return ''.join(res)
        