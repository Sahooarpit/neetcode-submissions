class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append((position[i], (target-position[i])/speed[i]))
        
        cars.sort(key = lambda x: x[0])

        fleets = 0
        
        currMax = 0.0
        
        while cars != []:
            time = cars.pop()[1]
            if currMax < time:
                fleets += 1
                currMax = time
        
        return fleets
            
