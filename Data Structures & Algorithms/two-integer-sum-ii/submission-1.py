class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l = 0
        r = len(numbers) - 1

        while l < r:
            soma = numbers[r] + numbers[l]
            if soma == target: return [l + 1, r + 1]
            elif soma > target:
                r -= 1
                continue
            else:
                l += 1
                continue
        
            

