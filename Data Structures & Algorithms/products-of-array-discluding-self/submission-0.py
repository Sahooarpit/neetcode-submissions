class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        curr = 1
        for i in nums:
            curr *= i
            prefix.append(curr)

        print(prefix)
        curr = 1

        for i in nums[::-1]:
            curr *= i 
            suffix.insert(0, curr)
        
        print(suffix)
        res = []

        res.append(suffix[1])

        for i in range(1, len(nums)-1):
            res.append(prefix[i-1]*suffix[i+1])
        
        res.append(prefix[-2])

        return res

        