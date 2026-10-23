class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def bs(l, r):
            if l > r:
                return -1
            
            if len(nums) == 0:
                return -1 

            middle =(l + r) // 2

            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                return bs(middle + 1, r)
            else:
                return bs(l, middle - 1)
        

        l = 0
        r = len(nums) - 1

        return bs(l, r)
        