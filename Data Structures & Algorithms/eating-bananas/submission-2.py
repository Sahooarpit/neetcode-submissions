class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        piles.sort()

        l = 1
        r = piles[-1]
        ans = 0
        while r >= l:

            mid = int((l+r)/2)
            time = 0
            for i in piles:
                time += math.ceil(i/mid)
            # print(l , r, mid, time)
            if time > h:
                l = mid + 1
            else:
                r = mid - 1
                ans = mid

            
        return ans

            