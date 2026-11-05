class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        n = len(digits)
        if n == 0:
            return []
        res = [""]
        maps = {"2":"abc",
                   "3":"def",
                   "4":"ghi",
                   "5":"jkl",
                   "6":"mno",
                   "7":"pqrs",
                   "8":"tuv",
                   "9":"wxyz"}
        
        for digit in digits:
            tmp = []
            for curStr in res:
                for c in maps[digit]:
                    tmp.append(curStr + c)
            res = tmp
        return res