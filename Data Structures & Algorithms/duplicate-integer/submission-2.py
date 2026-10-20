from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = Counter(nums)

        for x in nums:
            if freq[x] > 1: return True
        
        return False
        