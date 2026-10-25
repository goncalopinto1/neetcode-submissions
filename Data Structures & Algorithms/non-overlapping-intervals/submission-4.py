class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        s = sorted(intervals)

        upper = s[0][1]
        count = 0

        for i in range(1, len(s)):
            if upper > s[i][0]:#  intersetam-se
                count += 1
                upper = min(upper, s[i][1])
            else:
                upper = s[i][1]
                
        return count