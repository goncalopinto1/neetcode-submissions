class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = list()

        ordered = sorted(nums)
        for idx in range(len(ordered)): # fix this one

            if ordered[idx] > 0: # all after this one will also be positive
                break

            if idx > 0 and ordered[idx]  == ordered[idx - 1]:
                continue

            l = idx + 1
            r = len(ordered) - 1

            while l < r:
                soma = ordered[l] + ordered[r]

                if soma + ordered[idx] == 0: 
                    res.append([ordered[idx], ordered[l], ordered[r]])
                    r -= 1
                    l += 1

                    while l < r and ordered[l] == ordered[l - 1]:
                            l += 1

                elif soma > -ordered[idx]:
                    r -= 1
                
                else:
                    l += 1

        return [list(t) for t in res]