class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
    
        ans = []
        n = len(nums)

        def addNums(currSum, arr, ptr):
            
            if currSum < target:
                for i in range(ptr, n, 1):
                    addNums(currSum+ nums[i], arr + [nums[i]] , i)
            elif currSum == target:       
                ans.append(arr)
            
            return None
        
        addNums(0, [], 0)
        return ans