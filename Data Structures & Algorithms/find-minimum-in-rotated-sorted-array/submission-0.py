class Solution:
    def findMin(self, nums: List[int]) -> int:
        # rotating len(array) gives the same array

        # return the min elem of the array
        # the point is when n + 1 is lower than n

        l = 0
        r = len(nums) - 1

        while l < r:
            middle = (l + r) // 2

            if nums[middle] > nums[r]:
                l = middle + 1
                continue
            r = middle
        
        return nums[r]