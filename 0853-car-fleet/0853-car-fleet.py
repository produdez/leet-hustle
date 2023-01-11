class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
            Version 1
            
            Idea:
                1. Sort cars by position so that we can reduce the cars/result
                2. Keep adding car into fleet
                    - If reducible, reduce the fleet into the current car (furthest slowest car)
                    - If not reducible, just add as a new fleet
                    - Note that when a car can reduce a fleet, keep checking
            Complexity:
            - Time: O(nlogn)-sort + O(2n)-reduce fleet
            - Space: O(1) or O(n) for sorting + O(n) for fleet result
            
            Note: why O(2n) to reduce fleet
            - Cause we ilterate n times 
            - And everytime we can reduce we reduce
            - #reduce = #car
            -> so total reduce time is n
            -> 2n
        '''
        def catchable(x1,v1, x2, v2):
            if (x1-x2)*(v1-v2) >= 0: return False
            return (x1-x2)/(v2-v1) * v1 + x1 <= target

        cars = sorted(zip(position, speed), key=lambda x: x[0])        
        fleets = []
        for car in cars:
            while fleets and catchable(*car, *fleets[-1]):
                fleets.pop()
            fleets.append(car)
        return len(fleets)
            
            
                
            