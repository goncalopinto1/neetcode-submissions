class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()

        ordered = sorted(nums)
        for idx in range(len(ordered)): # fix this one

            l = idx + 1
            r = len(ordered) - 1

            while l < r:
                soma = ordered[l] + ordered[r]

                if soma + ordered[idx] == 0: 
                    res.add((ordered[idx], ordered[l], ordered[r]))
                    r -= 1
                    l += 1

                elif soma > -ordered[idx]:
                    r -= 1
                
                else:
                    l += 1

        return list(res)