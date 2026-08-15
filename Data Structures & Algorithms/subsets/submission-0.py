class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = [[]]

        for i in nums:
            copy = ans[::]
            for j in copy:
                copyj = j[::] + [i]
                ans.append(copyj)
                

        
        return ans

    