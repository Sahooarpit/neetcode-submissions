class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        #initialize board wit dots
        board = [["."]*n for _ in range(n)]
        #create 3 sets to reserve rows, cols and diagonals
        cols = [False]*n
        posDiag = [False]*(n*2)
        negDiag = [False]*(n*2)
        res = []
        #place queen on every row
        def dfs( r):
            nonlocal cols, posDiag, negDiag, res
            if r == n:
                temp = []
                for row in board:
                    temp.append("".join(row))
                res.append(temp)
                            

            for c in range(n):

                if cols[c] or posDiag[r+c] or negDiag[r-c+n]:
                    continue

                cols[c] = True
                posDiag[r+c] =True
                negDiag[r-c+n] = True
                board[r][c] = "Q"

                dfs(r+1)

                cols[c] = False
                posDiag[r+c] = False
                negDiag[r-c+n] = False
                board[r][c] = "."

        dfs(0)
        return res