class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # number of diff groups that arrive at the target at the same time
        # if x cars are in the same pos they will arrive at the same time -> 1

        # como saber se eles se econtram em alguma posição antes de target

        # (array de pos ao longo do tempo)
        stack = []

        counter = 0

        sorted_pos = sorted(zip(position, speed))

        for n in sorted_pos:
            number_steps = (target - n[0]) / n[1] 

            stack.append(number_steps)

        while stack:
            val = stack.pop()

            if stack and val >= stack[-1]:
                stack[-1] = val
            else:
                counter += 1
        
        return counter


        
        