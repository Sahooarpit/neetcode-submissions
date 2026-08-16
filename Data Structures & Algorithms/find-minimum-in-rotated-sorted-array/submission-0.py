class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        #possibilities - 123456 - l < mid < r      345612  mid > l  > r     561234  l > r > mid


        l = 0
        r = len(nums) - 1

        while l <= r:

            mid = (l+r)//2
            print(nums[mid])
            if nums[l] > nums[r]:
                if nums[mid] >= nums[l]:

                    l = mid + 1
                else:

                    r = mid
            
            else:

                return nums[l]
        

