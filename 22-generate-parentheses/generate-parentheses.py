class Solution:
  def generateParenthesis(self, n: int) -> List[str]:
    res = []
    def backtracking(value, open, close):
      if len(value) == 2 * n:
        res.append(str(value))
        return
      if open < n:
        backtracking(value + '(', open + 1, close)

      if close < open:
        backtracking(value + ')', open, close + 1)
        
    backtracking("", 0, 0)
    return res
        