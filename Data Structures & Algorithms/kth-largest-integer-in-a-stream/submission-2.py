import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.target = k
        self.stream = nums
        heapq.heapify(self.stream)
        print(self.stream)
        while len(self.stream) > k:      
            heapq.heappop(self.stream)
            print(self.stream)


    def add(self, val: int) -> int:
        
        if len(self.stream) < self.target:
            heapq.heappush(self.stream, val)
            return(self.stream[0])
        heapq.heappushpop(self.stream, val)
        return self.stream[0]
