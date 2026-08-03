class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for ind, i in enumerate(nums):
            if target - i in nums[ind+1:]:
                return [ind, nums[ind+1:].index(target-i)+ind+1]
            