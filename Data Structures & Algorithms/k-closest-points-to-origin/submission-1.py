import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        nums=[]
        
        for x,y in points:
            distance=math.sqrt(((x-0)**2)+((y-0)**2))
            nums.append([distance,x,y])
        
        heapq.heapify(nums)
        res=[]
        for i in range(k):
            d,a,b=heapq.heappop(nums)
            res.append([a,b])



        print(res)
        return res