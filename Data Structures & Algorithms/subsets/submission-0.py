class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, atual):
            if i > len(nums) - 1:
                res.append(atual[:])
                return
            
            atual.append(nums[i])
            backtrack(i + 1, atual)
            atual.pop()
            backtrack(i + 1, atual)
            
        backtrack(0, [])

        return res