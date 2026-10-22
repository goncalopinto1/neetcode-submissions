class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        
        op = {"+": lambda a, b: a + b,
              "-": lambda a, b: a - b,
              "*": lambda a, b: a * b,
              "/": lambda a, b: int(a / b)
              }

        for n in tokens:
            if n in op:
                val1 = operands.pop()
                val2 = operands.pop()

                func = op[n]

                res = func(val2, val1)

                operands.append(res)
            else:
                operands.append(int(n))
            
        return operands.pop()
                