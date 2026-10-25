from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        s = sorted(hand)
        c = Counter(hand)

        for n in s:
            if c[n] > 0: # é a mais pequena logo inicia um grupo
                c[n] -= 1
                
                for i in range(1, groupSize):
                    if c[n + i] == 0:
                        return False
                    c[n + i] -= 1
        
        if any(x > 0 for x in c.values()):
            return False

        return True

        

