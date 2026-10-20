from collections import defaultdict
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums) 
        postfix = [0] * len(nums) 
        
        res = [0] * len(nums) 

        acc = 1;

        for i in range(len(nums)):
            acc *= nums[i]

            prefix[i] = acc;


        acc = 1

        for i in reversed(range(len(nums))):
            acc *= nums[i]

            postfix[i] = acc

        
        for i in range(len(nums)):
            if i == 0:
                nums[i] = postfix[i + 1]
            elif i == len(nums) - 1:
                nums[i] = prefix[i - 1]
            else:
                nums[i] = prefix[i - 1] * postfix[i + 1]
        
        return nums




            