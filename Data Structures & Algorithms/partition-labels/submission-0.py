from collections import Counter
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        c = Counter(s)

        size = 0
        seen = set()
        res = []

        for ch in s:
            size += 1

            seen.add(ch)

            c[ch] -= 1
            
            if c[ch] == 0:
                del c[ch]
            else:
                continue
            
            if not any(x in c for x in seen):
                res.append(size)
                size = 0
            
            
        return res