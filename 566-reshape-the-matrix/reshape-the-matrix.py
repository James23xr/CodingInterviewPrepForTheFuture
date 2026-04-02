class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if m*n != r*c:
            return mat
        res = [[0]*c for _ in range(r)]
        new_r = 0
        new_c = 0
        for row in range(m):
            for col in range(n):
                res[new_r][new_c] = mat[row][col]
                new_c +=1
                if new_c ==c:
                    new_r += 1
                    new_c = 0
        return res

                

        