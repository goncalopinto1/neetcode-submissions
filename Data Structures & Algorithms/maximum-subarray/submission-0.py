class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum  = nums[0]
        s = 0
        for n in nums:
            if s <= 0 and n > s:
                s = n
            else:
                s += n
            max_sum = max(max_sum, s)
        return max_sum