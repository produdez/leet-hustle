class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
            Version 2.5: Update simplicity + intuition
                update no need stack and can keep track by arrive time of fleet
            Idea:
                1. sort by position
                2. GO FROM RIGHT TO LEFT
                3. If reducible, reduce to the fleet head (the slower right car)
                4. reducible can be check by compare arrive time to target
            Complexity:
            - Time: O(nlogn)-sort + O(n) fleet build
            - Space: O(n) for sorted array
        '''

        cars = sorted(zip(position, speed), reverse=True)  
        fleet_count = 1
        arrive_time = lambda car: (target - car[0]) / car[1]
        fleet_time = arrive_time(cars[0])
        for i in range(1, len(cars)):
            arr_time = arrive_time(cars[i])
            if fleet_time >= arr_time:
                continue
            fleet_count += 1
            fleet_time = arr_time
        return fleet_count
            
            
                
            