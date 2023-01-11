class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
            Version 2: Update simplicity + intuition
            
            Idea:
                1. sort by position
                2. GO FROM RIGHT TO LEFT
                3. If reducible, reduce to the fleet head (the slower right car)
                4. reducible can be check by compare arrive time to target
            Complexity:
            - Time: O(nlogn)-sort + O(n) fleet build
            - Space: O(n) for sorted array + O(n) for stack
        '''

        cars = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)       
        fleets = []
        catchable = lambda c1, c2: (target-c2[0])/c2[1] >= (target-c1[0])/c1[1]
        
        for car in cars:
            if fleets and catchable(car, fleets[-1]):
                continue
            fleets.append(car)
        return len(fleets)
            
            
                
            