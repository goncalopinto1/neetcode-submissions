class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []


        res = [0] * len(temperatures)

        for i in range(len(temperatures)):

            if stack:
                while stack and temperatures[i] > stack[-1][0]: 
                    val = stack.pop()

                    res[val[1]] = (i - val[1])
                
                stack.append((temperatures[i], i))
                count = 0
            else:
                stack.append((temperatures[i], i))

        return res