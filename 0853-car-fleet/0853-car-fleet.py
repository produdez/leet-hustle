class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), key=lambda x: x[0])
        def catchable(car1, car2):
            x1,v1 = car1
            x2, v2 = car2
            if x1==x2: return True
            if (x1-x2)*(v1-v2) >= 0: return False
            meet = (x1-x2)/(v2-v1) * v1 + x1
            if meet > target: return False
            return True
        
        stack = [cars[0]]
        for car in cars[1:]:
            while stack and catchable(car, stack[-1]):
                car2 = stack.pop()
                car = car if car[1] < car2[1] else car2
            stack.append(car)
        return len(stack)
            
            
                
            