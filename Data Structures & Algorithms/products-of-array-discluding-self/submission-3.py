class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        acc = 1

        for i in range(len(nums)):
            if i == 0:
                res[i] *= 1
            else:
                res[i] *= acc
            acc *= nums[i]

        acc = 1

        for i in reversed(range(len(nums))):
            if i == len(nums) - 1:
                res[i] *= 1
            else:
                res[i] *= acc
            acc *= nums[i]

        return res
    



            