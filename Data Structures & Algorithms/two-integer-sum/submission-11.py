
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = dict()

        for idx, n in enumerate(nums):
            if target - n in d.keys(): return [d[target - n], idx]
            else: d[n] = idx
            