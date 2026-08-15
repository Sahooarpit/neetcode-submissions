class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []
        n = len(candidates)
        candidates.sort()
        def findSum(currSum, ptr, arr):

            if currSum < target:
                for i in range(ptr, n):
                    if i > ptr and candidates[i] == candidates[i-1]:
                        continue
                
                    if currSum + candidates[i] > target:
                        break  
                    
                    findSum(currSum + candidates[i], i+1, arr + [candidates[i]])

            elif currSum == target:
                    ans.append(arr)
            
            return None
        
        findSum(0, 0, [])

        return ans
