class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        s = sorted(intervals)

        res = []
        current = s[0]

        for i in range(1, len(intervals)):
            if s[i][0] <= s[i-1][1] or s[i][0] <= current[1]: # dao overlap
                current[1] = max(s[i][1], s[i-1][1], current[1])
            else:
                res.append(current)
                current = s[i]
        if len(current) > 0:
            res.append(current)
        return res
                