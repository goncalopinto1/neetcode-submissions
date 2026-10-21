class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = set(nums)

        best = 0

        for n in nums:
            size = 0
            if n - 1 not in values: # é o incício de uma seq
                curr = n
                size += 1
                while curr + 1 in values:
                    size += 1
                    curr += 1
                if size > best: best = size
            
        return best
