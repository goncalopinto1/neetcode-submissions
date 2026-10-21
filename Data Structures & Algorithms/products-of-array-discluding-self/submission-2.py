class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)

        res = [0] * len(nums)

        acc = 1

        for i in range(len(nums)):
            prefix[i] = acc * nums[i]
            acc *= nums[i]

        acc = 1

        for i in reversed(range(len(nums))):
            postfix[i] = acc * nums[i]
            acc *= nums[i]

        for i in range(len(nums)):
            if i == 0:
                res[i] = postfix[i + 1]
            elif i == len(nums) - 1:
                res[i] = prefix[i - 1]
            else:
                res[i] = prefix[i - 1] * postfix[i + 1]
        
        return res


    



            