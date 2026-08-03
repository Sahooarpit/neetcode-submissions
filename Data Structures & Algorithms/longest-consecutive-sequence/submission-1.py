class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        ans = 0
        for i in numSet:
            if i - 1 in numSet:
                continue
            currLargest = 1

            while i + currLargest in numSet:
                currLargest += 1
            
            ans = max(ans, currLargest)
        
        return ans