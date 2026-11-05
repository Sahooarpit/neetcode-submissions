class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        n = len(digits)
        if n == 0:
            return []
        res = []
        wordMap = {"2":"abc",
                   "3":"def",
                   "4":"ghi",
                   "5":"jkl",
                   "6":"mno",
                   "7":"pqrs",
                   "8":"tuv",
                   "9":"wxyz"}
        
        def dfs(pos, combination):
            if pos == n:
                res.append(combination)
                return
            for i in wordMap[digits[pos]]:
                combination += i
                dfs(pos+1, combination)
                combination = combination[:-1]
        
        dfs(0, "")
        return res