class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        visited = set()
        rows = len(board)
        cols = len(board[0])

        def dfs(wordInd, pos):

            if wordInd == len(word) -1:
                return True
            
            #if not the last index then chack all non visited index around it

            for r, c in [(-1, 0), (1, 0), (0, -1), (0, 1)]:

                r += pos[0]
                c+= pos[1]

                if  r < 0 or r == rows or c < 0 or c == cols:
                    continue
                
                if (r, c) not in visited and board[r][c] == word[wordInd+1]:
                    visited.add((r, c))
                    found = dfs(wordInd+1, (r, c))
                    visited.remove((r, c))
                    if found:
                        return True
                
            return False
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    visited.add((i, j))
                    if dfs(0, (i, j)):
                        return True
                    visited.remove((i,j))
        
        return False
