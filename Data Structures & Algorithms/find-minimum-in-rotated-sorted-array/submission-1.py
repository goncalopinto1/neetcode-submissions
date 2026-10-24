class Solution:
    def findMin(self, nums: List[int]) -> int:
        # middle > r entao down middle up down
        # else -> up down middle up

        l = 0
        r = len(nums) - 1

        while l < r:
            middle = (l + r) // 2

            if nums[middle] > nums[r]:
                l = middle + 1
            else:
                r = middle
        
        return nums[r]