class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        s = sorted(intervals)

        res = []
        n = list(s[0])
        current = n

        for i in range(1, len(intervals)):
            if s[i][0] <= current[1]: # dao overlap
                current[1] = max(s[i][1], current[1])
            else:
                res.append(current)
                n = list(s[i])
                current = n
        if len(current) > 0:
            res.append(current)
        return res
                