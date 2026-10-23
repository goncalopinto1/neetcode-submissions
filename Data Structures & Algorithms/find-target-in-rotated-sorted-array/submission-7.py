class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            middle = (l + r) // 2

            if nums[middle] == target: # a break happened
                return middle
            elif nums[middle] > nums[r]:
                if nums[l] <= target < nums[middle]:
                    r = middle - 1
                else:
                    l = middle + 1
            else:
                if nums[r] >= target > nums[middle]:
                    l = middle + 1
                else:
                    r = middle - 1

        
        if nums[r] == target:
            return r

        return -1