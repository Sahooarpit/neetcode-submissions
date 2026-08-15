class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        ptr1 = 0
        ptr2 = len(heights) - 1
        ans = 0

        while ptr1 != ptr2:
            ans = max(ans, (ptr2-ptr1)*min(heights[ptr1], heights[ptr2]))

            if heights[ptr1] < heights[ptr2]:
                ptr1 +=1
            else:
                ptr2 -= 1
            
        return ans