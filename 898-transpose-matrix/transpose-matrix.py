class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        m,n = len(matrix), len(matrix[0])
        res = [[0]*m for _ in range(n)]
        for r in range(m):
            for c in range(n):
                res[c][r] = matrix[r][c]
        return res
        