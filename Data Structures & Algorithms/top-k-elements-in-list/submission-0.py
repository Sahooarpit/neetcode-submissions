class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = defaultdict(int)

        for i in nums:
            count[i] += 1
        
        frq = [[] for i in range(len(nums)+1)]

        for i in count.keys():
            frq[count[i]].append(i)
        
        res = []
        for i in frq[::-1]:
            for j in i:
                res.append(j)
                if len(res) == k:
                    return res