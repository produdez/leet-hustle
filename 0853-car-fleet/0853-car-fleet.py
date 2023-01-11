class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        def catchable(x1,v1, x2, v2):
            if (x1-x2)*(v1-v2) >= 0: return False
            return (x1-x2)/(v2-v1) * v1 + x1 <= target

        cars = sorted(zip(position, speed), key=lambda x: x[0])        
        stack = []
        for car in cars:
            while stack and catchable(*car, *stack[-1]):
                stack.pop()
            stack.append(car)
        return len(stack)
            
            
                
            