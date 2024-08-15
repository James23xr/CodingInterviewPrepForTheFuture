class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return [["Q"]]
        if n == 2 or n == 3:
            return []

        results = []
        solution = [-1] * n
        self.solveNQueensRec(n, solution, 0, results)
        return results

    def solveNQueensRec(
        self, n: int, solution: List[int], row: int, results: List[List[str]]
    ):
        if row == n:
            results.append(self.constructSolutionString(solution))
            return

        for col in range(n):
            if self.isValidMove(row, col, solution):
                solution[row] = col
                self.solveNQueensRec(n, solution, row + 1, results)
                solution[row] = -1  # Backtrack

    def isValidMove(
        self, proposedRow: int, proposedCol: int, solution: List[int]
    ) -> bool:
        for i in range(proposedRow):
            oldRow = i
            oldCol = solution[i]
            diagonalOffset = proposedRow - oldRow

            if (
                oldCol == proposedCol
                or oldCol == proposedCol - diagonalOffset
                or oldCol == proposedCol + diagonalOffset
            ):
                return False
        return True

    def constructSolutionString(self, solution: List[int]) -> List[str]:
        board = []
        for row in range(len(solution)):
            row_str = ["."] * len(solution)
            row_str[solution[row]] = "Q"
            board.append("".join(row_str))
        return board