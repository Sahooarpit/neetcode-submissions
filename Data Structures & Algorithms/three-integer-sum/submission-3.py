class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ans = []
        for i in range(0, len(nums)-2):
            if i != 0 and nums[i] == nums[i-1]:
                continue

            target = -nums[i]
            start = i + 1
            end = len(nums)-1

            while start < end:
                if nums[start] + nums[end] == target:
                    ans.append([nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1
                    while nums[start] == nums[start-1] and start < end:
                        start += 1
                elif nums[start] + nums[end] > target:
                    end -= 1
                    
                else:
                    start += 1

               
        
        return ans